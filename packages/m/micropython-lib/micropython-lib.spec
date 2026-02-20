#
# spec file for package micropython-lib
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           micropython-lib
Version:        1.27.0
Release:        0
Summary:        Core Python libraries ported to MicroPython
License:        MIT AND Python-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/micropython/micropython-lib
Source:         https://github.com/micropython/micropython-lib/archive/v%{version}.tar.gz#/micropython-lib-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/micropython/micropython/refs/tags/v%{version}/tools/manifestfile.py
Source2:        https://raw.githubusercontent.com/micropython/micropython/refs/tags/v%{version}/mpy-cross/mpy_cross/__init__.py#/mpy_cross.py
Patch1:         access_index_from_local_fs.patch
BuildRequires:  fdupes
BuildArch:      noarch
BuildRequires:  micropython
BuildRequires:  mpy-tools
BuildRequires:  python3

%description
micropython-lib is a project to develop a non-monolothic standard library for MicroPython.
Each module or package is available as a separate distribution package from PyPI.
Each module is either written from scratch or ported from CPython.

%prep
%autosetup -p1 -n micropython-lib-%{version}

# prepare build.py dependencies
cp %SOURCE1 ./tools/manifestfile.py
mkdir tools/mpy_cross
cp %SOURCE2 ./tools/mpy_cross/__init__.py

# bootstrap mip
mkdir mip
cp -r micropython/mip/mip/* mip/
cp -r micropython/mip-cmdline/mip/* mip/

%build
# build mip index
python3 ./tools/build.py --mpy-cross %{_bindir}/mpy-cross --output ./mip_index

%install
# install all pkgs from index
for pkg in $(python3 -c 'import json;[print(p["name"]) for p in json.load(open("mip_index/index.json"))["packages"]]') ; do
	micropython -m mip install --no-mpy -t %{buildroot}%{_prefix}/lib/micropython -i file://mip_index "$pkg"
done

# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find %{buildroot}%{_prefix}/lib/micropython -name "*.py" -exec sed -i 's|#! %{_bindir}/env python3|#!%{_bindir}/python3|' {} ";"
find %{buildroot}%{_prefix}/lib/micropython -name "*.py" -exec sed -i 's|#! %{_prefix}/local/bin/python|#!%{_bindir}/python3|' {} ";"
# Fix permissions
chmod 0755 %{buildroot}%{_prefix}/lib/micropython/{base64,keyword,quopri,uu}.py
# Run fdupes
%fdupes %{buildroot}%{_prefix}/lib/micropython

%check
# check that we can import a module that we just installed and that it actually works
cd %{buildroot}%{_prefix}/lib/micropython
micropython -c 'import hashlib; s=hashlib.sha384("foo").hexdigest(); assert s.startswith("98c11ffdf")'

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/micropython

%changelog
