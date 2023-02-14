#
# spec file for package skelcd-openSUSE
#
# Copyright (c) 2023 SUSE LLC
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


%define version_unconverted 84.87.20230105.e1eb746
# changed by pre_checkin
%define is_non_oss 0
#
%if 0%{?suse_version} >= 1500 && !0%{?skelcd_compat}
%define skelcdpath %{_prefix}/lib/skelcd
%endif
#
%bcond_with betatest
%bcond_without  java
#
Name:           skelcd-openSUSE
Version:        84.87.20230105.e1eb746
Release:        0
Summary:        Skeleton for openSUSE OSS Media Sets
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/skelcd-openSUSE
Source:         skelcd-openSUSE-%{version}.tar.xz
Source99:       skelcd-openSUSE-rpmlintrc
BuildRequires:  build-key
Conflicts:      skelcd-openSUSE-non-OSS
Conflicts:      skelcd-openSUSE-non-OSS-CD
Conflicts:      skelcd-sled
Conflicts:      skelcd-sles
%if %{with java}
BuildRequires:  release-notes-openSUSE
# we abuse the no java path here to skip license processing in staging
BuildRequires:  translate-toolkit
%endif

%description
Internal package only, used for openSUSE OSS Media sets

%package non-OSS
Summary:        Skeleton for openSUSE non-OSS Media Sets
Group:          Metapackages

%description non-OSS
Internal package only, used for openSUSE non-OSS Media sets

%prep
%setup -q
%if ! %{with betatest}
  # Remove README.BETA unless we build a beta version (prjconf flag)
  rm skelcd/README.BETA
%endif

%build
DIST="%{distribution}"
DISTVER=${DIST#openSUSE }
if [ "$DISTVER" = 'Factory' ]; then
  DISTVER=Tumbleweed
fi
sed -i -e"s@#VERSION#@$DISTVER@g" license/license.txt
%if %{with java}
make %{?_smp_mflags} VERSION="$DISTVER"
%else
# build without translate-toolkit support in staging
make %{?_smp_mflags} VERSION="$DISTVER" LICENSES=
%endif
#

%install
mkdir -p %{buildroot}%{?skelcdpath}/CD1/boot
# YaST uses release notes txt for textmode installation and rtf for graphical
%if %{with java}
  mkdir -p %{buildroot}%{?skelcdpath}/CD1/docu
  cp -p %{_datadir}/doc/release-notes/openSUSE/RELEASE-NOTES.*.{rtf,txt} %{buildroot}%{?skelcdpath}/CD1/docu
%endif
#
cp skelcd/* %{buildroot}%{?skelcdpath}/CD1/
cp skelcd/.treeinfo.%suse_version %{buildroot}%{?skelcdpath}/CD1/.treeinfo
install -m 644 %{_prefix}/lib/rpm/gnupg/keys/*.asc %{buildroot}%{?skelcdpath}/CD1/
# treeinfo file for virt-install

%files
%if %{defined skelcdpath}
%dir %{skelcdpath}
%endif
%{?skelcdpath}/CD1

%files non-OSS
%if %{defined skelcdpath}
%dir %{skelcdpath}
%endif
%{?skelcdpath}/CD1
%exclude %{?skelcdpath}/CD1/docu
%exclude %{?skelcdpath}/CD1/license.tar.gz
%exclude %{?skelcdpath}/CD1/.treeinfo

%changelog
