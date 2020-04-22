#
# spec file for package python2-pip
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
Requires(post): update-alternatives
Requires(postun): update-alternatives
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

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/pip
ln -sf %{_sysconfdir}/alternatives/pip \
     %{buildroot}%{_bindir}/pip

%fdupes %{buildroot}%{python2_sitelib}

%post
# can't use `python_install_alternative` because it's pipX.Y, not pip-X.Y
%{_sbindir}/update-alternatives --install %{_bindir}/pip \
    pip %{_bindir}/pip2.7 27

%postun
if [ ! -f %{_bindir}/pip ] ; then
    %{_sbindir}/update-alternatives --remove pip %{_bindir}/pip2.7
fi

%files
%license LICENSE.txt
%doc AUTHORS.txt NEWS.rst README.rst
%ghost %{_sysconfdir}/alternatives/pip
%{_bindir}/pip%{python2_version}
%{_bindir}/pip
%{_bindir}/pip2
%{python2_sitelib}/pip-%{version}-py*.egg-info
%{python2_sitelib}/pip

%changelog
