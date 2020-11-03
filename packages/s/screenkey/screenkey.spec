#
# spec file for package screenkey
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


Name:           screenkey
Version:        1.2
Release:        0
Summary:        A screen-cast tool to show keys
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            https://www.thregr.org/~wavexx/software/screenkey/
Source0:        https://www.thregr.org/~wavexx/software/screenkey/releases/%{name}-%{version}.tar.gz
Source1:        https://www.thregr.org/~wavexx/software/screenkey/releases/%{name}-%{version}.tar.gz.asc
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-git
Requires:       python3
Requires:       python-gtk
Requires:       python3-pycairo
Requires:       slop
Recommends:     fontawesome-fonts
BuildArch:      noarch

%description
A screencast tool to show keys. Inspired by Screenflick and based on
the key-mon project.

%prep
%autosetup

%build
CFLAGS="%{optflags}" %python_exec setup.py build

%install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}
find build/lib* -name '*.py' -exec sed -i "1{/^#!/d}" {} + && \
%python_exec setup.py install -O1 --skip-build --root %{buildroot} --prefix %{_prefix}/
%fdupes -s %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python_sitelib}/Screenkey
%{python_sitelib}/%{name}-%{version}-py3.8.egg-info
%doc %{_datadir}/doc/%{name}/

%changelog
