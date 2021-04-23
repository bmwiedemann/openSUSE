#
# spec file for package unrar_wrapper
#
# Copyright (c) 2020 SUSE LLC
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


Name:           unrar_wrapper
Version:        1.0.0
Release:        0
Summary:        Backwards compatibility between unar and unrar
License:        GPL-3.0-only
Group:          Productivity/Archiving/Compression
URL:            https://github.com/openSUSE/unrar_wrapper
Source:         https://github.com/openSUSE/unrar_wrapper/archive/unrar_wrapper-%{version}.tar.gz
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
Requires:       unar
Conflicts:      unrar
Provides:       unrar
BuildArch:      noarch

%description
Wrapper python script that transforms the basic UnRAR commands to unar
and lsar calls in order to provide a backwards compatibility.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
python3 setup.py build

%check
python3 setup.py test

%install
python3 setup.py install --root=%{buildroot}
ln -s %{_bindir}/unrar_wrapper %{buildroot}/%{_bindir}/unrar

%files
%license LICENSE
%doc README.md
%{_bindir}/unrar_wrapper
%{_bindir}/unrar
%{python3_sitelib}/unrar_wrapper.py
%{python3_sitelib}/__pycache__
%{python3_sitelib}/unrar_wrapper-%{version}-py%{py3_ver}.egg-info

%changelog
