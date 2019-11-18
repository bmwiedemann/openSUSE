#!/usr/bin/env python3

# Copyright 2013, 2014 Red Hat, Inc., and William C. Benton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import xml.etree.ElementTree as ET
import argparse
import re
import logging

from io import StringIO
from os.path import exists as pathexists
from os.path import realpath
from os.path import join as pathjoin
from os import makedirs
from os import symlink
from os import remove as rmfile
from shutil import copyfile
from javapackages.xmvn.xmvn_resolve import (XMvnResolve, ResolutionRequest)

class Artifact(object):
    def __init__(self, a, g, v):
        self.artifact = a
        self.group = g
        self.version = v
    
    @classmethod
    def fromCoords(k, coords):
        g,a,v = coords.split(":")
        return k(a, g, v)
    
    @classmethod
    def fromSubtree(k, t, ns):
        a = t.find("./%sartifactId" % ns).text
        g = t.find("./%sgroupId" % ns).text
        v = t.find("./%sversion" % ns).text
        return k(a, g, v)
    
    def contains(self, substrings):
        for s in substrings:
            if s in self.artifact or s in self.group:
                cn_debug("ignoring %r because it contains %s" % (self, s))
                return True
        if len(substrings) > 0:
            cn_debug("not ignoring %r; looked for %r" % (self, substrings))
        return False
    
    def __repr__(self):
        return "%s:%s:%s" % (self.group, self.artifact, self.version)

class DummyPOM(object):
    def __init__(self, groupID=None, artifactID=None, version=None):
        self.groupID = groupID
        self.artifactID = artifactID
        self.version = version
        self.deps = []

def interestingDep(dt, namespace):
    if len(dt.findall("./%soptional" % namespace)) != 0:
        cn_debug("ignoring optional dep %r" % Artifact.fromSubtree(dt, namespace))
        return False
    if [e for e in dt.findall("./%sscope" % namespace) if e.text == "test"] != []:
        cn_debug("ignoring test dep %r" % Artifact.fromSubtree(dt, namespace))
        return False
    return True

class POM(object):
    def __init__(self, filename, suppliedGroupID=None, suppliedArtifactID=None, ignored_deps=[], override=None, extra_deps=[]):
        self.filename = filename
        self.sGroupID = suppliedGroupID
        self.sArtifactID = suppliedArtifactID
        self.logger = logging.getLogger("com.freevariable.climbing-nemesis")
        self.deps = []
        self.ignored_deps = ignored_deps
        self.extra_deps = extra_deps
        cn_debug("POM:  extra_deps is %r" % extra_deps)
        self._parsePom()
        self.claimedGroup, self.claimedArtifact  = override is not None and override or (self.groupID, self.artifactID)
    
    def _parsePom(self):
        tree = ET.parse(self.filename)
        project = tree.getroot()
        self.logger.info("parsing POM %s", self.filename)
        self.logger.debug("project tag is '%s'", project.tag)
        tagmatch = re.match("[{](.*)[}].*", project.tag)
        namespace = tagmatch and "{%s}" % tagmatch.groups()[0] or ""
        self.logger.debug("looking for '%s'", ("./%sgroupId" % namespace))
        groupIDtag = project.find("./%sgroupId" % namespace) 
        if groupIDtag is None:
            groupIDtag = project.find("./%sparent/%sgroupId" % (namespace,namespace))
        
        versiontag = project.find("./%sversion" % namespace)
        if versiontag is None:
            versiontag = project.find("./%sparent/%sversion" % (namespace,namespace))
        self.logger.debug("group ID tag is '%s'", groupIDtag)
        self.groupID = groupIDtag.text
        self.artifactID = project.find("./%sartifactId" % namespace).text
        self.version = versiontag.text
        depTrees = project.findall(".//%sdependencies/%sdependency" % (namespace, namespace))
        alldeps = [Artifact.fromSubtree(depTree, namespace) for depTree in depTrees if interestingDep(depTree, namespace)]
        alldeps = [dep for dep in alldeps if not (dep.group == self.groupID and dep.artifact == self.artifactID)]
        self.deps = [dep for dep in alldeps if not dep.contains(self.ignored_deps)] + [Artifact.fromCoords(xtra) for xtra in self.extra_deps]
        jarmatch = re.match(".*JPP-(.*).pom", self.filename)
        self.jarname = (jarmatch and jarmatch.groups()[0] or None)

def cn_debug(*args):
    logging.getLogger("com.freevariable.climbing-nemesis").debug(*args)

def cn_info(*args):
    logging.getLogger("com.freevariable.climbing-nemesis").info(*args)

def resolveArtifact(group, artifact, pomfile=None, ignored_deps=[], override=None, extra_deps=[]):
    # XXX: some error checking would be the responsible thing to do here
    cn_debug("rA:  extra_deps is %r" % extra_deps)
    if pomfile is None:
        result = XMvnResolve.process_raw_request([ResolutionRequest(group, artifact, extension="pom")])[0]
        if result:
            return POM(result.artifactPath, ignored_deps=ignored_deps, override=override, extra_deps=extra_deps)
        else:
            return DummyPOM(group, artifact)
    else:
        return POM(pomfile, ignored_deps=ignored_deps, override=override, extra_deps=extra_deps)

def resolveJar(group, artifact):
    result = XMvnResolve.process_raw_request([ResolutionRequest(group, artifact)])[0]
    return result.artifactPath if result else None

def makeIvyXmlTree(org, module, revision, status="release", meta={}, deps=[]):
    ivy_module = ET.Element("ivy-module", {"version":"1.0", "xmlns:e":"http://ant.apache.org/ivy/extra"})
    info = ET.SubElement(ivy_module, "info", dict({"organisation":org, "module":module, "revision":revision, "status":status}.items() | meta.items()))
    info.text = " " # ensure a close tag
    confs = ET.SubElement(ivy_module, "configurations")
    for conf in ["default", "provided", "test"]:
        ET.SubElement(confs, "conf", {"name":conf})
    pubs = ET.SubElement(ivy_module, "publications")
    ET.SubElement(pubs, "artifact", {"name":module, "type":"jar"})
    if len(deps) > 0:
        deptree = ET.SubElement(ivy_module, "dependencies")
        for dep in deps:
            ET.SubElement(deptree, "dependency", {"org":dep.group, "name":dep.artifact, "rev":dep.version})
    return ET.ElementTree(ivy_module)

def writeIvyXml(org, module, revision, status="release", fileobj=None, meta={}, deps=[]):
    # XXX: handle deps!
    if fileobj is None:
        fileobj = StringIO()
    tree = makeIvyXmlTree(org, module, revision, status, meta=meta, deps=deps)
    tree.write(fileobj, xml_declaration=True)
    return fileobj

def ivyXmlAsString(org, module, revision, status, meta={}, deps=[]):
    return writeIvyXml(org, module, revision, status, meta=meta, deps=deps).getvalue()

def placeArtifact(artifact_file, repo_dirname, org, module, revision, status="release", meta={}, deps=[], supplied_ivy_file=None, scala=None, override=None, override_dir_only=False):
    if scala is not None:
        module = module + "_%s" % scala
    jarmodule = module
    if override is not None:
        org, module = override
        if not override_dir_only:
            jarmodule = module
    repo_dir = realpath(repo_dirname)
    artifact_dir = pathjoin(*[repo_dir] + [org] + [module, revision])
    ivyxml_path = pathjoin(artifact_dir, "ivy.xml")
    artifact_repo_path = pathjoin(artifact_dir, "%s-%s.jar" % (jarmodule, revision))
    
    if not pathexists(artifact_dir):
        makedirs(artifact_dir)
    
    ivyxml_file = open(ivyxml_path, "wb")
    if supplied_ivy_file is None:
        writeIvyXml(org, module, revision, status, ivyxml_file, meta=meta, deps=deps)
    else:
        copyfile(supplied_ivy_file, ivyxml_path)
    
    if pathexists(artifact_repo_path):
        rmfile(artifact_repo_path)
    
    symlink(artifact_file, artifact_repo_path)

def main():
    parser = argparse.ArgumentParser(description="Place a locally-installed artifact in a custom local Ivy repository; get metadata from Maven")
    parser.add_argument("group", metavar="GROUP", type=str, help="name of group")
    parser.add_argument("artifact", metavar="ARTIFACT", type=str, help="name of artifact")
    parser.add_argument("repodir", metavar="REPO", type=str, help="location for local repo")
    parser.add_argument("--version", metavar="VERSION", type=str, help="version to advertise this artifact as, overriding Maven metadata")
    parser.add_argument("--meta", metavar="K=V", type=str, help="extra metadata to store in ivy.xml", action='append')
    parser.add_argument("--jarfile", metavar="JAR", type=str, help="local jar file (use instead of POM metadata")
    parser.add_argument("--pomfile", metavar="POM", type=str, help="local pom file (use instead of xmvn-resolved one")
    parser.add_argument("--log", metavar="LEVEL", type=str, help="logging level")
    parser.add_argument("--ivyfile", metavar="IVY", type=str, help="supplied Ivy file (use instead of POM metadata)")
    parser.add_argument("--scala", metavar="VERSION", type=str, help="encode given scala version in artifact name")
    parser.add_argument("--ignore", metavar="STR", type=str, help="ignore dependencies whose artifact or group contains str", action='append')
    parser.add_argument("--override", metavar="ORG:NAME", type=str, help="override organization and/or artifact name")
    parser.add_argument("--override-dir-only", action='store_true', help="override organization and/or artifact name")
    parser.add_argument("--extra-dep", metavar="ORG:NAME:VERSION", action='append', help="add the given dependencya")
    args = parser.parse_args()
    
    if args.log is not None:
        logging.basicConfig(level=getattr(logging, args.log.upper()))
    
    override = args.override and args.override.split(":") or None
    cn_debug("cl: args.extra_dep is %r" % args.extra_dep)
    extra_deps = args.extra_dep is not None and args.extra_dep or []
    
    pom = resolveArtifact(args.group, args.artifact, args.pomfile, ignored_deps=(args.ignore or []), override=((not args.override_dir_only) and override or None), extra_deps=extra_deps)
    
    if args.jarfile is None:
        jarfile = resolveJar(pom.groupID or args.group, pom.artifactID or args.artifact)
    else:
        jarfile = args.jarfile
    
    version = (args.version or pom.version)
    
    meta = dict([kv.split("=") for kv in (args.meta or [])])
    cn_debug("meta is %r" % meta)
    
    placeArtifact(jarfile, args.repodir, pom.groupID, pom.artifactID, version, meta=meta, deps=pom.deps, supplied_ivy_file=args.ivyfile, scala=args.scala, override=override, override_dir_only=args.override_dir_only)

if __name__ == "__main__":
    main()
