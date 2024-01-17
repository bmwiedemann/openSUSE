#
# spec file for package python2-pip
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


Name:           python2-pip
Version:        20.0.2
Release:        0
Summary:        A Python package management system
License:        MIT
URL:            http://www.pip-installer.org
Source:         https://github.com/pypa/pip/archive/%{version}.tar.gz
Patch0:         pip-shipped-requests-cabundle.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-setuptools
Requires:       ca-certificates
Requires:       coreutils
Requires:       python2-setuptools
Requires(pre):  update-alternatives
Recommends:     ca-certificates-mozilla
BuildArch:      noarch

%description
Pip is a replacement for pip. It uses mostly the same techniques for
finding packages, so packages that were made pipable should be
pip-installable as well.

%prep
%setup -q -n pip-%{version}
%autopatch -p1

# remove shebangs verbosely (if only sed would offer a verbose mode...)
for f in $(find src -name \*.py -exec grep -l '^#!%{_bindir}/env' {} \;); do
    sed -i 's|^#!%{_bindir}/env .*$||g' $f
done
rm src/pip/_vendor/certifi/cacert.pem

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python2_sitelib}

%pre
# remove previous u-a usage early so an update of pip packages for python3 does not fail
# boo#1194429
if [ ! -f %{_bindir}/pip ] ; then
    %{_sbindir}/update-alternatives --remove pip %{_bindir}/pip2.7
fi

%files
%license LICENSE.txt
%doc AUTHORS.txt NEWS.rst README.rst
%{_bindir}/pip%{python2_version}
%exclude %{_bindir}/pip
%{_bindir}/pip2
%{python2_sitelib}/pip-%{version}-py*.egg-info
%{python2_sitelib}/pip

%changelog
