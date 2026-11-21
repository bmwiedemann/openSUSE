#
# spec file for package modelcontextprotocol-servers
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license of this file is the same as for the package itself
# unless otherwise specified. Please submit bugfixes or comments via
# https://bugs.opensuse.org/
#


%global __nodejs_provides %{nil}
%global __nodejs_requires %{nil}
%define appdir %{_datadir}/%{name}
%define fast_uri_version 3.1.9
Name:           modelcontextprotocol-servers
Version:        2.5.0
Release:        0
Summary:        Model Context Protocol reference servers
# the MCP SDK inlines ajv and friends (MIT) and fast-uri (BSD-3-Clause), its docs are CC-BY-4.0;
# diff and qs are BSD-3-Clause, minimatch is BlueOak-1.0.0, the rest MIT or ISC
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND ISC AND BlueOak-1.0.0 AND CC-BY-4.0
URL:            https://github.com/modelcontextprotocol/servers
Source0:        https://github.com/modelcontextprotocol/servers/archive/refs/tags/v%{version}.tar.gz#/servers-%{version}.tar.gz
Source1:        prune-workspace.mjs
# package-lock.json is upstream's, reduced with prune-lock.py
Source2:        prune-lock.py
Source3:        replace-fast-uri.mjs
Source4:        check-servers.mjs
Source5:        https://registry.npmjs.org/fast-uri/-/fast-uri-%{fast_uri_version}.tgz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
# licenses of the modules the MCP SDK inlines
Source20:       https://raw.githubusercontent.com/ajv-validator/ajv/v8.18.0/LICENSE#/LICENSE.ajv
Source21:       https://raw.githubusercontent.com/ajv-validator/ajv-formats/v3.0.1/LICENSE#/LICENSE.ajv-formats
Source22:       https://raw.githubusercontent.com/cfworker/cfworker/@cfworker/json-schema@4.1.1/LICENSE.md#/LICENSE.cfworker-json-schema
Source23:       https://raw.githubusercontent.com/epoberezkin/fast-deep-equal/v3.1.3/LICENSE#/LICENSE.fast-deep-equal
Source24:       https://raw.githubusercontent.com/epoberezkin/json-schema-traverse/v1.0.0/LICENSE#/LICENSE.json-schema-traverse
Source99:       %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  local-npm-registry
BuildRequires:  nodejs >= 24
BuildRequires:  typescript >= 5.8.2
Requires:       nodejs >= 24
BuildArch:      noarch
%include %{_sourcedir}/node_modules.spec.inc

%description
Reference servers of the Model Context Protocol (MCP). This package holds
the Node.js modules the servers share at runtime.

%package -n mcp-server-everything
Summary:        MCP test server exercising all protocol features
License:        Apache-2.0 AND MIT AND CC-BY-4.0
Requires:       %{name} = %{version}-%{release}

%description -n mcp-server-everything
A Model Context Protocol server that exercises the features of the
protocol: prompts, resources, tools, sampling, elicitation and logging,
over the stdio, SSE or streamable HTTP transport. It is a test server for
developers of MCP clients and not meant for production use.

%package -n mcp-server-filesystem
Summary:        MCP server for filesystem operations
License:        Apache-2.0 AND MIT AND CC-BY-4.0
Requires:       %{name} = %{version}-%{release}

%description -n mcp-server-filesystem
A Model Context Protocol server to read, write, search and move files and
directories. Access is limited to the directories given on the command
line.

%package -n mcp-server-memory
Summary:        MCP server providing a persistent knowledge graph memory
License:        Apache-2.0 AND MIT AND CC-BY-4.0
Requires:       %{name} = %{version}-%{release}

%description -n mcp-server-memory
A Model Context Protocol server that keeps entities, relations and
observations in a knowledge graph stored as a JSON lines file, so a client
can remember information across sessions.

The graph is kept in $XDG_DATA_HOME/mcp-server-memory/memory.jsonl, by
default under ~/.local/share. Set MEMORY_FILE_PATH to the absolute path of
another file to use.

%package -n mcp-server-sequential-thinking
Summary:        MCP server for step-by-step problem solving
License:        Apache-2.0 AND MIT AND CC-BY-4.0
Requires:       %{name} = %{version}-%{release}

%description -n mcp-server-sequential-thinking
A Model Context Protocol server providing a tool for dynamic and reflective
problem solving through a structured, revisable sequence of thoughts.

%prep
%autosetup -n servers-%{version} -a 5
# pins the registry to npmjs.org, overriding the local one
rm .npmrc
cp %{SOURCE10} package-lock.json
node %{SOURCE1}
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts
# the SDK was built with fast-uri 3.1.8
node %{SOURCE3} 3.1.8 %{fast_uri_version} package
cp package/LICENSE LICENSE.fast-uri
cp %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} .

%build
for ws in everything filesystem memory sequentialthinking; do
  tsc -p src/$ws
done
# served as resources
cp -a src/everything/docs src/everything/dist/
# prune resolves the tree anew, like the install did
local-npm-registry %{_sourcedir} prune --omit=dev --ignore-scripts

%install
mkdir -p %{buildroot}%{appdir} %{buildroot}%{_bindir}
cp -a node_modules %{buildroot}%{appdir}/
# the workspace links point back into the build tree
find %{buildroot}%{appdir}/node_modules -type l -delete
rm %{buildroot}%{appdir}/node_modules/.package-lock.json
find %{buildroot}%{appdir}/node_modules -type d -empty -delete
for ws in everything filesystem memory sequentialthinking; do
  mkdir -p %{buildroot}%{appdir}/$ws
  cp -a src/$ws/package.json src/$ws/dist %{buildroot}%{appdir}/$ws/
done
# nothing reads these at runtime
find %{buildroot}%{appdir} \( -name '*.map' -o -name '*.min.js' -o -name '*.d.ts' -o -name '*.d.cts' -o -name '*.d.mts' \) -delete
rm -r %{buildroot}%{appdir}/node_modules/zod/src
find %{buildroot}%{appdir}/node_modules -name '.*' -prune -exec rm -r {} +
find %{buildroot}%{appdir} -type f -exec chmod 0644 {} +
chmod 0755 %{buildroot}%{appdir}/*/dist/index.js
sed -i '1s|^#!%{_bindir}/env node$|#!%{_bindir}/node|' %{buildroot}%{appdir}/*/dist/index.js
# a module of index.js, not a command
sed -i '1{/^#!/d}' %{buildroot}%{appdir}/everything/dist/transports/stdio.js
cat > %{buildroot}%{_bindir}/mcp-server-memory <<'EOF'
#!/bin/sh
# the default next to the server code is not writable
if [ -z "$MEMORY_FILE_PATH" ]; then
  case "$XDG_DATA_HOME" in
    /*) data=$XDG_DATA_HOME ;;
    *) data=${HOME:?}/.local/share ;;
  esac
  MEMORY_FILE_PATH="$data/mcp-server-memory/memory.jsonl"
  mkdir -p "${MEMORY_FILE_PATH%%/*}"
fi
export MEMORY_FILE_PATH
exec %{_bindir}/node %{appdir}/memory/dist/index.js "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/mcp-server-memory
ln -s %{appdir}/everything/dist/index.js %{buildroot}%{_bindir}/mcp-server-everything
ln -s %{appdir}/filesystem/dist/index.js %{buildroot}%{_bindir}/mcp-server-filesystem
ln -s %{appdir}/sequentialthinking/dist/index.js %{buildroot}%{_bindir}/mcp-server-sequential-thinking
%fdupes %{buildroot}%{appdir}/node_modules

# vitest needs prebuilt esbuild/rollup binaries, so call the installed servers
%check
unset MEMORY_FILE_PATH
# a relative XDG_DATA_HOME is not valid and must not be used
export HOME=$PWD/check-home XDG_DATA_HOME=relative
sed 's|%{appdir}|%{buildroot}%{appdir}|' %{buildroot}%{_bindir}/mcp-server-memory > check-memory
chmod 0755 check-memory
node %{SOURCE4} ./check-memory \
  'create_entities={"entities":[{"name":"rpm-check","entityType":"package","observations":["built"]}]}' \
  'read_graph={}'
grep -q rpm-check check-home/.local/share/mcp-server-memory/memory.jsonl
node %{SOURCE4} %{buildroot}%{appdir}/sequentialthinking/dist/index.js \
  'sequentialthinking={"thought":"check","thoughtNumber":1,"totalThoughts":1,"nextThoughtNeeded":false}'
node %{SOURCE4} %{buildroot}%{appdir}/everything/dist/index.js \
  'echo={"message":"rpm-check"}'
# the HTTP transports load express, cors and hono
node --input-type=module -e '
for (const transport of ["sse", "streamableHttp"]) await import(`%{buildroot}%{appdir}/everything/dist/transports/${transport}.js`);
process.exit(0);'
mkdir check-files
echo rpm-check > check-files/file
printf '#!/bin/sh\nexec %{buildroot}%{appdir}/filesystem/dist/index.js "$PWD/check-files"\n' > check-filesystem
chmod 0755 check-filesystem
node %{SOURCE4} ./check-filesystem \
  "read_text_file={\"path\":\"$PWD/check-files/file\"}" > check-filesystem.out
grep -q rpm-check check-filesystem.out
# content-type is installed with its license, the others have theirs in the main package
test "$(grep -rhoE '^//#region .*/\.pnpm/[^/]+' %{buildroot}%{appdir}/node_modules/@modelcontextprotocol | sed 's|.*/||' | LC_ALL=C sort -u | tr '\n' ' ')" = \
  "@cfworker+json-schema@4.1.1 ajv-formats@3.0.1_ajv@8.18.0 ajv@8.18.0 content-type@1.0.5 fast-deep-equal@3.1.3 fast-uri@%{fast_uri_version} json-schema-traverse@1.0.0 "
# only the replaced fast-uri refuses a percent-encoded scheme
cd %{buildroot}%{appdir}/memory
node --input-type=module -e '
import { createRequire } from "node:module";
const shims = "@modelcontextprotocol/server/_shims";
for (const { DefaultJsonSchemaValidator } of [await import(shims), createRequire(process.cwd() + "/")(shims)]) {
  let message;
  try {
    new DefaultJsonSchemaValidator().getValidator({ $id: "%%61:b" });
  } catch (error) {
    message = error.message;
  }
  if (!message?.includes("URI scheme is malformed")) throw new Error(`fast-uri not replaced: ${message}`);
}'

%files
%license LICENSE LICENSE.*
%dir %{appdir}
%{appdir}/node_modules

%files -n mcp-server-everything
%doc src/everything/CHANGELOG.md src/everything/README.md
%{_bindir}/mcp-server-everything
%{appdir}/everything

%files -n mcp-server-filesystem
%doc src/filesystem/CHANGELOG.md src/filesystem/README.md
%{_bindir}/mcp-server-filesystem
%{appdir}/filesystem

%files -n mcp-server-memory
%doc src/memory/CHANGELOG.md src/memory/README.md
%{_bindir}/mcp-server-memory
%{appdir}/memory

%files -n mcp-server-sequential-thinking
%doc src/sequentialthinking/CHANGELOG.md src/sequentialthinking/README.md
%{_bindir}/mcp-server-sequential-thinking
%{appdir}/sequentialthinking

%changelog
