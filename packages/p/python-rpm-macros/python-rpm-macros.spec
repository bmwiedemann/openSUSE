#
# spec file for package python-rpm-macros
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-rpm-macros
Version:        20240415.c664b45
Release:        0
Summary:        RPM macros for building of Python modules
License:        WTFPL
URL:            https://github.com/opensuse/python-rpm-macros
Source:         python-rpm-macros-%{version}.tar.xz
# To keep user expectations reasonably sane
Recommends:     python-rpm-generators
# Fedora compatibility
Provides:       python2-rpm-macros
Provides:       python3-rpm-macros
BuildArch:      noarch

%description
This package contains SUSE RPM macros for Python build automation.
You should BuildRequire this package unless you are sure that you
are only building for distros newer than Leap 42.2

%package -n python-rpm-generators
Summary:        Dependency generator dependencies for Python RPMs
Requires:       %{name} = %{version}-%{release}
# For the dep generator macros
Requires:       python3-setuptools
# Fedora compatibility
Provides:       python3-rpm-generators

%description -n python-rpm-generators
This package contains the dependencies for Python RPMs to generate
dependencies automatically.

%prep
%autosetup

%if 0%{?suse_version} < 1330
mv macros-default-pythons macros/035-default-pythons
%endif
%if 0%{?suse_version} >= 1550
sed -i -e '/^%system_python/s/python2/python3/' macros/010-common-defs
%endif

%build
./compile-macros.sh

%install
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
install -m 644 macros.python_all %{buildroot}%{_rpmconfigdir}/macros.d/

%files
%license LICENSE
%doc README.md
%{_rpmconfigdir}/macros.d/macros.python_all

%files -n python-rpm-generators
# Nothing here for now...

%changelog
