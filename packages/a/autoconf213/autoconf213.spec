#
# spec file for package autoconf213
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           autoconf213
Url:            http://www.gnu.org/software/autoconf
BuildRequires:  m4 >= 1.1
Requires:       gawk
Requires:       m4 >= 1.1
Requires:       mktemp
Requires:       perl
%if %suse_version > 1140
BuildRequires:  makeinfo
%endif
PreReq:         %{install_info_prereq}
Version:        2.13
Release:        0
Summary:        A GNU Tool for Automatically Configuring Source Code
License:        GPL-2.0+
Group:          Development/Tools/Building
BuildArch:      noarch
Source:         http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz
Patch0:         autoconf-2.12-race.patch
Patch1:         autoconf-2.13-mawk.patch
Patch2:         autoconf-2.13-notmp.patch
Patch3:         autoconf-2.13-c++exit.patch
Patch4:         autoconf-2.13-headers.patch
Patch5:         autoconf-2.13-autoscan.patch
Patch6:         autoconf-2.13-exit.patch
Patch7:         autoconf-2.13-wait3test.patch
Patch8:         autoconf-2.13-make-defs-62361.patch
Patch9:         autoconf-2.13-versioning.patch
Patch10:        autoconf213-destdir.patch
Patch11:        autoconf213-info.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNU Autoconf is a tool for configuring source code and makefiles. Using
autoconf, programmers can create portable and configurable packages,
because the person building the package is allowed to specify various
configuration options.

You should install autoconf if you are developing software and would
like to create shell scripts to configure your source code packages.

Note that the autoconf package is not required for the end user who may
be configuring software with an autoconf-generated script; autoconf is
only required for the generation of the scripts, not their use.

%prep
%setup -n autoconf-%{version} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
mv autoconf.texi autoconf213.texi
rm -f autoconf.info

%build
./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir} \
            --program-suffix=-2.13
make %{?_smp_mflags}

%install
%makeinstall
# We don't want to include the standards.info stuff in the package,
# because it comes from binutils...
rm -f ${RPM_BUILD_ROOT}%{_infodir}/standards*

%post
%install_info --info-dir=%{_infodir} %{_infodir}/autoconf213.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/autoconf213.info.gz

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_prefix}/bin/*
%{_prefix}/share/autoconf-2.13
%doc %{_infodir}/autoconf213.info.gz

%changelog
