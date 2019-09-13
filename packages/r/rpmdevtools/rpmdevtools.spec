#
# spec file for package rpmdevtools
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define emacs_sitestart_d %{_datadir}/emacs/site-lisp
Name:           rpmdevtools
Version:        8.10
Release:        0
Summary:        RPM Development Tools
# rpmdev-setuptree is GPL-2.0, everything else GPL-2.0+
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://pagure.io/rpmdevtools
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.xz
Source1:        skeleton
Source2:        %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE suse-specfile.patch -- Apply fix to comply to http://en.opensuse.org/openSUSE:Specfile_guidelines
Patch0:         suse-specfile.patch
Patch1:         dont-drop-Groups.patch
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  rpm-python
BuildRequires:  xz
BuildRequires:  pkgconfig(bash-completion)
# Required for bash-completion
Requires:       bash-completion
# Additionally required for tool operations
Requires:       cpio
Requires:       curl
# Minimal RPM build requirements
Requires:       distribution-release
Requires:       fakeroot
Requires:       python
Requires:       rpm-python
BuildArch:      noarch

%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5/sha*     Display checksums of all files in an archive file
rpmdev-vercmp       RPM version comparison checker
spectool            Expand and download sources and patches in specfiles
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
rpmdev-bumpspec     Bump revision in specfile
...and many more.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp -a %{SOURCE1} template.init

# Use the "rpmdev-" prefix for spectool that conflicts with Redhat spectool
sed -i "s/spectool/rpmdev-spectool/g" rpmdevtools.bash-completion.in spectool.in

%build
%configure --libdir=%{_libexecdir}
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{emacs_sitestart_d}
ln -s %{_datadir}/rpmdevtools/rpmdev-init.el %{buildroot}%{emacs_sitestart_d}/rpmdev-init.el
#/bin/touch %%{buildroot}%%{emacs_sitestart_d}/rpmdev-init.elc

# Use the "rpmdev-" prefix for spectool that conflicts with Redhat spectool
mv %{buildroot}%{_bindir}/spectool %{buildroot}%{_bindir}/rpmdev-spectool
mv %{buildroot}%{_mandir}/man1/spectool.1 %{buildroot}%{_mandir}/man1/rpmdev-spectool.1

# Fix rpmlint warning "non-executable-script"
chmod 755 %{buildroot}%{_datadir}/rpmdevtools/{trap.sh,tmpdir.sh}

%files
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_bindir}/rpm*
%{_mandir}/man[18]/rpm*.[18]%{ext_man}
%{emacs_sitestart_d}/rpmdev-init.el*
%{_datadir}/rpmdevtools/
%{_datadir}/bash-completion/completions/*

%changelog
