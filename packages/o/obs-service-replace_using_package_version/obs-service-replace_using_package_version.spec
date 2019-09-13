#
# spec file for package obs-service-replace_with_package_version
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%define service replace_using_package_version

Name:           obs-service-%{service}
Version:        0.0.3
Release:        0
Summary:        An OBS service: Replaces a regex  with the version value of a package
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
Url:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{service}.tar
%if 0%{?suse_version} > 1315
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
Requires:       python3-docopt
%else
BuildRequires:  python-setuptools
Requires:       python-setuptools
Requires:       python-docopt
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This service replaces a given regex with the version value of
a given package. Can be used to align the version of you package or image
to the version of another package.

%prep
%setup -q -n %{service}

%build
%if 0%{?suse_version} > 1315
# Build Python 3 version
python3 setup.py build
%else
# Build Python 2 version
python2 setup.py build
%endif

%install
%if 0%{?suse_version} > 1315
# Install Python 3 version
python3 setup.py install --root %{buildroot} \
    --install-script %{_prefix}/lib/obs/service \
    --install-data %{_prefix}/lib/obs/service
%else
# Install Python 2 version
python2 setup.py install --root %{buildroot} \
    --install-script %{_prefix}/lib/obs/service \
    --install-data %{_prefix}/lib/obs/service
%endif

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service

%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif

%changelog
