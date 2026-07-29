#
# spec file for package laszip
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019 Bruno Friedmann, Ioda-Net Sàrl, Charmoille, Switzerland.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define         sover 8
Name:           laszip
Version:        3.5.0
Release:        0
Summary:        Compression library supporting ASPRS LAS format data
License:        LGPL-2.1-or-later
URL:            https://laszip.org/
# Upstream stopped attaching a release tarball (and its .sha256sum) at 3.5.0;
# the git auto-archive is the only published artifact.
Source0:        https://github.com/LASzip/LASzip/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A free product of rapidlasso GmbH - quickly turns bulky LAS files into
compact LAZ files without information loss. LASzip is a compression library that
was developed by Martin Isenburg for compressing ASPRS LAS format data in his
LAStools. It has been provided as an LGPL-licensed stand-alone software library
to allow other softwares that handle LAS data to read and write LASzip-compressed
data. The BSD-licensed libLAS and the LGPL-licensed LASlib can take advantage of
LASzip to read and write compressed data.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
A free product of rapidlasso GmbH - quickly turns bulky LAS files into
compact LAZ files without information loss. LASzip is a compression library that
was developed by Martin Isenburg for compressing ASPRS LAS format data in his
LAStools. It has been provided as an LGPL-licensed stand-alone software library
to allow other softwares that handle LAS data to read and write LASzip-compressed
data. The BSD-licensed libLAS and the LGPL-licensed LASlib can take advantage of
LASzip to read and write compressed data.

This package contain only the dynamic build.

%package -n lib%{name}_api%{sover}
Summary:        API library files for lib%{name}
# Packager comment are we sure this api can live alone ?
#Requires:       lib%%{name}%%{sover} = %%{version}

%description -n lib%{name}_api%{sover}
API library for %{name}
This package contain only the dynamic build.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}_api%{sover} = %{version}

%description devel
Headers and development files for %{name} needed to develop
softwares that handle LAS data to read and write LASzip-compressed
data.

%prep
%autosetup -p1 -n LASzip-%{version}
# Upstream ships README.md with CRLF line endings
sed -i 's/\r$//' README.md

%build
# laszip need dlopen,dlsym,dlclose
%cmake \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_C_FLAGS="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_CXX_FLAGS="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_CXX_FLAGS_RELWITHDEBINFO="%{optflags} -fno-strict-aliasing -fPIC" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -Wl,--no-as-needed -ldl"

%cmake_build

%install
%cmake_install

%check
# Upstream ships no test suite -- the only fixtures in data/ are LAZ files
# that are deliberately corrupt in a different way each. Use them for what
# they are for: every one must be *rejected* through the public C API rather
# than crash or be silently accepted, which is the regression these files
# exist to catch.
cat > smoke.c <<'EOF'
#include <laszip_api.h>
#include <stdio.h>
int main(int argc, char **argv)
{
    int i, bad = 0;
    /* liblaszip_api is a dlopen wrapper around liblaszip -- nothing works
       until the DLL is loaded, so this also exercises the -ldl link. */
    if (laszip_load_dll()) { fprintf(stderr, "laszip_load_dll failed\n"); return 1; }
    for (i = 1; i < argc; i++) {
        laszip_POINTER h = 0;
        laszip_BOOL compressed = 0;
        if (laszip_create(&h)) { fprintf(stderr, "create failed\n"); return 1; }
        if (laszip_open_reader(h, argv[i], &compressed) == 0) {
            fprintf(stderr, "FAIL: %s was accepted but is corrupt\n", argv[i]);
            bad = 1;
        } else {
            fprintf(stderr, "ok: %s rejected\n", argv[i]);
        }
        laszip_destroy(h);
    }
    return bad;
}
EOF
gcc %{optflags} -o smoke smoke.c -Idll -Iinclude/laszip -Lbuild/%{_lib} -llaszip_api
LD_LIBRARY_PATH=build/%{_lib} ./smoke data/*.laz

%ldconfig_scriptlets -n lib%{name}%{sover}
%ldconfig_scriptlets -n lib%{name}_api%{sover}

%files devel
%license COPYING.txt
%doc CHANGES.txt AUTHORS.txt README.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_api.so

%files -n lib%{name}%{sover}
%license COPYING.txt
%doc CHANGES.txt AUTHORS.txt README.md
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}_api%{sover}
%license COPYING.txt
%doc CHANGES.txt AUTHORS.txt README.md
%{_libdir}/lib%{name}_api.so.*

%changelog
