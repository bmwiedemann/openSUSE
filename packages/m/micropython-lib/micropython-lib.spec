#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" != "testsuite"
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}
%endif
Name:           micropython-lib%{name_suffix}
Version:        1.9.3
Release:        0
Summary:        Core Python libraries ported to MicroPython
License:        MIT AND Python-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/micropython/micropython-lib
Source:         https://github.com/micropython/micropython-lib/archive/v%{version}.tar.gz#/micropython-lib-%{version}.tar.gz
BuildRequires:  fdupes
BuildArch:      noarch
%if "%{flavor}" == "testsuite"
BuildRequires:  micropython
BuildRequires:  micropython-lib
%endif

%description
micropython-lib is a project to develop a non-monolothic standard library for MicroPython.
Each module or package is available as a separate distribution package from PyPI.
Each module is either written from scratch or ported from CPython.

%prep
%setup -q -n micropython-lib-%{version}

%build
%if "%{flavor}" != "testsuite"
%make_build
%endif

%install
%if "%{flavor}" != "testsuite"
%make_install PREFIX=%{buildroot}%{_prefix}/lib/micropython
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find %{buildroot}%{_prefix}/lib/micropython -name "*.py" -exec sed -i 's|#! %{_bindir}/env python3|#!%{_bindir}/python3|' {} ";"
find %{buildroot}%{_prefix}/lib/micropython -name "*.py" -exec sed -i 's|#! %{_prefix}/local/bin/python|#!%{_bindir}/python3|' {} ";"
# Fix permissions
chmod 0755 %{buildroot}%{_prefix}/lib/micropython/{base64,cgi,keyword,quopri,timeit,uu}.py
# Run fdupes
%fdupes %{buildroot}%{_prefix}/lib/micropython
%endif

%if "%{flavor}" == "testsuite"
%check
micropython -v ./test/test_pep380.py
%endif

%if "%{flavor}" != "testsuite"
%files
%license LICENSE
%{_prefix}/lib/micropython
%endif

%changelog
