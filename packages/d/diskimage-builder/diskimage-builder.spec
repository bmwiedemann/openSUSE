#
# spec file for package diskimage-builder
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Prevent shebangs of element scripts from being added as a requirement (they
# are only ever run inside the disk image build chroot).
%global         __requires_exclude_from ^%{python3_sitelib}/diskimage_builder/elements/.*$
Name:           diskimage-builder
Version:        2.28.0
Release:        0
Summary:        Image Building Tools for OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/openstack/diskimage-builder
Source0:        https://pypi.io/packages/source/d/%{name}/%{name}-%{version}.tar.gz
Source99:       diskimage-builder-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  python3-PyYAML >= 3.10.0
BuildRequires:  python3-networkx >= 1.10
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
# Test requirements (python2 only)
BuildRequires:  python2-PyYAML >= 3.10.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-networkx >= 1.10
BuildRequires:  python2-oslotest
BuildRequires:  python2-stevedore >= 1.20.0
BuildRequires:  python2-testrepository
BuildRequires:  python2-testtools
BuildRequires:  sed
# No stuff in python_sitelib, thus autoreqprov won't work:
Requires:       kpartx
Requires:       python3-Babel >= 2.3.4
Requires:       python3-PyYAML >= 3.10.0
Requires:       python3-networkx >= 1.10
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
Requires:       qemu-tools
Requires:       sudo
BuildArch:      noarch

%description
diskimage-builder is a tool for automatically building customized
operating-system images for use in clouds and other environments.

It includes support for building images based on many major
distributions and can produce cloud-images in all common formats
(qcow2, vhd, raw, etc), bare metal file-system images and ram-disk
images. These images are composed from the many included elements;
diskimage-builder acts as a framework to easily add your own elements
for even further customization.

%prep
%setup -q
# Remove <2.6.0 which is incompatible with python-flake8
# dib-lint uses flake8, but does not appear incompatible with flake8 v3.x
sed -i 's/^flake8<.*/flake8/' requirements.txt

# Fix env-script-interpreter rpmlint warning
find diskimage_builder/elements -type f -perm /a+x \
	-exec sh -c "sed -E -i s@^#\!%{_bindir}/env[[:space:]]+python@#\!%{_bindir}/python@ {}" \;

%build
%python3_build

%install
%python3_install
%py3_compile %{buildroot}
%fdupes %{buildroot}

%check
if [ ! -d ./.testrepository ] ; then testr init ; fi
testr run %{?_smp_mflags:--parallel %{_smp_flags}} #; RET=$? echo "Slowest Tests" ; testr slowest && exit $RET

%files
%doc ChangeLog README.rst AUTHORS
%license LICENSE
%{_bindir}/dib-block-device
%{_bindir}/disk-image-create
%{_bindir}/dib-lint
%{_bindir}/element-info
%{_bindir}/ramdisk-image-create
%{python3_sitelib}/diskimage_builder/
%{python3_sitelib}/diskimage_builder*.egg-info/

%changelog
