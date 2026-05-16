from javapackages.maven.pom import POM, PomLoadingException

from javapackages.xmvn.xmvn_resolve import (XMvnResolve, ResolutionRequest,
                                            XMvnResolveException)
from javapackages.common.exception import JavaPackagesToolsException

import sys
import os

def get_parent_pom(pom):

    req = ResolutionRequest(pom.groupId, pom.artifactId,
                            extension="pom", version=pom.version)
    result = XMvnResolve.process_raw_request([req])[0]
    if not result:
        raise XMvnResolveException("Unable to resolve parent POM {g}:{a}:{e}:{v}"
                                   .format(g=pom.groupId, a=pom.artifactId,
                                           e="pom", v=pom.version))

    return POM(result.artifactPath)


def gather_properties(pom_path):
    pom = POM(pom_path)
    props = pom.properties

    curr_pom = pom
    parent = pom.parent
    while parent:
        ppom = None
        if hasattr(parent, "relativePath") and parent.relativePath != "":
            try:
                ppom_path = os.path.join(os.path.dirname(curr_pom._path),
                                         parent.relativePath)
                if os.path.isdir(ppom_path):
                    ppom_path = os.path.join(ppom_path, 'pom.xml')
                ppom = POM(ppom_path)
            except PomLoadingException:
                pass
        else:
            try:
                ppom_path = os.path.join(os.path.dirname(curr_pom._path), '..')
                if os.path.isdir(ppom_path):
                    ppom_path = os.path.join(ppom_path, 'pom.xml')
                ppom = POM(ppom_path)
            except PomLoadingException:
                pass

        if not ppom:
            try:
                ppom = get_parent_pom(parent)
            except XMvnResolveException:
                break

        parent = ppom.parent
        pprops = ppom.properties

        # merge "properties" sections
        for pkey in pprops:
            if pkey not in props:
                props[pkey] = pprops[pkey]

        curr_pom = ppom

    return props


def _main():
    if not os.path.exists(sys.argv[1]):
        message = ("The first argument '{0}' doesn't point to an existing file ").format(sys.argv[1])
        parser.error(message)

    pom_path = sys.argv[1]

    props = gather_properties(pom_path)

    for key, value in props.items():
        print(f"{key}={value}")

if __name__ == "__main__":
    try:
        _main()
    except JavaPackagesToolsException as e:
        sys.exit(e)
