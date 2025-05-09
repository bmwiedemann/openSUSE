#
# spec file for package rpmconf
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rpmconf
Version:        1.1.11
Release:        0
Summary:        Tool to handle rpmnew and rpmsave files
License:        GPL-3.0-or-later
URL:            https://github.com/xsuchy/rpmconf
Source:         https://github.com/xsuchy/%{name}/archive/%{name}-%{version}-1.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  docbook-utils-minimal
BuildRequires:  docbook_3
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-rpm
BuildRequires:  python3-setuptools
Requires:       python3-%{name}
Requires:       python3-rpm
Suggests:       diffuse
Suggests:       diffutils
Suggests:       kdiff3
Suggests:       meld
Suggests:       vim
BuildArch:      noarch

%description
This tool search for .rpmnew, .rpmsave and .rpmorig files and ask
you what to do with them:
Keep current version, place back old version, watch the diff or merge.

%package -n python3-%{name}
Summary:        Python interface for rpmconf
Group:          Development/Languages/Python

%description -n python3-%{name}
Python interface for rpmconf and an essential part of rpmconf.

%prep
%autosetup -n %{name}-%{name}-%{version}-1

sed -i 's/__version__ = .*/__version__ = "%{version}"/' rpmconf/rpmconf.py
sed -i 's/version = .*,/version = "%{version}",/' setup.py

%build
%python3_build
docbook2man %{name}.sgml
%make_build -C docs man \
  SPHINXBUILD=sphinx-build-%{py3_ver}

%install
%python3_install --skip-build --install-scripts %{_sbindir}

chmod a+x %{buildroot}%{python3_sitelib}/%{name}/%{name}.py
install -Dpm 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
install -Dpm 0644 docs/build/man/%{name}.3 %{buildroot}%{_mandir}/man3/%{name}.3
mkdir -p %{buildroot}%{_datadir}/%{name}/
find docs/build/ -type f -name ".buildinfo" -delete -print

%fdupes -s %{buildroot}%{python3_sitelib}

%files
%license LICENSES/GPL-3.0-only.txt
%doc README.md TODO
%{_sbindir}/%{name}
%dir %{_datadir}/%{name}/
%{_mandir}/man8/%{name}.8%{?ext_man}

%files -n python3-%{name}
%license LICENSES/GPL-3.0-only.txt
%doc README.md TODO
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-*.egg-info
%{_mandir}/man3/%{name}.3%{?ext_man}

%changelog
