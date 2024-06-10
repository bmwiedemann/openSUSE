#
# spec file for package Modules
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


Name:           Modules
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  less
BuildRequires:  procps
BuildRequires:  tcl-devel
URL:            http://modules.sourceforge.net/
Version:        4.8.0
Release:        0
Summary:        Change environment at runtime
License:        GPL-2.0-or-later
Group:          System/Management
Requires:       python3
Requires:       tcl
Source:         https://download.sourceforge.net/project/modules/Modules/modules-%{version}/modules-%{version}.tar.gz
Patch1:         Remove-empty-unused-static-function.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       environment-modules
%if 0%{?suse_version}
Recommends:     %{name}-doc
%endif

%if 0%{?rhel_version} || 0%{?fedora_version}
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
%endif

%description
The Modules package is a tool that simplify shell initialization and lets
users easily modify their environment during the session with modulefiles.

Each modulefile contains the information needed to configure the shell for an
application. Once the Modules package is initialized, the environment can be
modified on a per-module basis using the module command which interprets
modulefiles. Typically modulefiles instruct the module command to alter or set
shell environment variables such as PATH, MANPATH, etc. modulefiles may be
shared by many users on a system and users may have their own collection to
supplement or replace the shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an clean
fashion. All popular shells are supported, including bash, ksh, zsh, sh, csh,
tcsh, fish, as well as some scripting languages such as tcl, perl, python,
ruby, cmake and r.

Modules are useful in managing different versions of applications. Modules can
also be bundled into metamodules that will load an entire suite of different
applications.

%package doc
Summary:        Documentation for Environment Modules
Group:          Documentation/Other
BuildArch:      noarch

%description doc
The Modules package is a tool that simplify shell initialization and lets
users easily modify their environment during the session with modulefiles.

Each modulefile contains the information needed to configure the shell for an
application. Once the Modules package is initialized, the environment can be
modified on a per-module basis using the module command which interprets
modulefiles. Typically modulefiles instruct the module command to alter or set
shell environment variables such as PATH, MANPATH, etc. modulefiles may be
shared by many users on a system and users may have their own collection to
supplement or replace the shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an clean
fashion. All popular shells are supported, including bash, ksh, zsh, sh, csh,
tcsh, fish, as well as some scripting languages such as tcl, perl, python,
ruby, cmake and r.

Modules are useful in managing different versions of applications. Modules can
also be bundled into metamodules that will load an entire suite of different
applications.

%define vimdatadir %{_datadir}/vim/site

%prep
%autosetup -p1 -n modules-%{version}

# This is debatable:
# if the replace 'bash' consecutive calls to 'modules' would still
# run with the original bash. Maybe not intended.
sed -i 's@/usr/bin/env bash@/bin/bash@' script/envml

%build
./configure \
    --initdir="%{_datadir}/%name/init" \
    --libexecdir="%{_prefix}/%_lib/%{name}/" \
    --prefix="%_prefix" \
    --with-version-path="%_datadir/%{name}" \
    --modulefilesdir="%{_datadir}/modules" \
    --mandir=%{_mandir} \
    --with-etc-path="%_sysconfdir" \
    --with-skel-path="%_sysconfdir/skel" \
    --with-tcl=%{_libdir} \
    %{?!vimdatadir: --disable-vim-addons} \
    %{?vimdatadir: --vimdatadir=%{vimdatadir}} \
    --etcdir=%{_sysconfdir}/%{name} \
    --libdir=%{_libdir}/%{name} \
    --enable-compat-version \
    --with-python=/usr/bin/python3
make %{?_smp_mflags}

%install
install -d %{buildroot}/usr/share/modules
install -d %{buildroot}/etc/profile.d
make DESTDIR=%{buildroot} install
install -d %{buildroot}/usr/bin
mv %{buildroot}/usr/share/doc doc_dir
%fdupes -s %{buildroot}%{_datadir}

ln -sf %{_datadir}/Modules/init/profile.sh %{buildroot}%{_sysconfdir}/profile.d/modules.sh
ln -sf %{_datadir}/Modules/init/profile.csh %{buildroot}%{_sysconfdir}/profile.d/modules.csh

mkdir -p %{buildroot}%{_datadir}/fish/{vendor_completions.d,vendor_functions.d}
ln -sf %{_datadir}/Modules/init/fish_completion %{buildroot}%{_datadir}/fish/vendor_completions.d/module.fish
ln -sf %{_datadir}/Modules/init/fish %{buildroot}%{_datadir}/fish/vendor_functions.d/module.fish

%files
%defattr(-,root,root)
%doc doc_dir/README
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/modules
%config %{_sysconfdir}/%{name}
%{_bindir}/add.modules
%{_bindir}/envml
%{_bindir}/mkroot
%{_bindir}/modulecmd
%{_bindir}/createmodule.py
%{_datadir}/%{name}/init
%{?vimdatadir:%dir %{dirname:%{?vimdatadir}}}
%{?vimdatadir}
%{_libdir}/%{name}/modulecmd-compat
%{_libdir}/%{name}/modulecmd.tcl
%{_libdir}/%{name}/libtclenvmodules.so
%{_datadir}/modules/*
%{_mandir}/man1/module-compat.1*
%{_mandir}/man1/ml.1*
%{_mandir}/man1/module.1*
%{_mandir}/man4/modulefile-compat.4*
%{_mandir}/man4/modulefile.4*
%{_sysconfdir}/profile.d/modules.sh
%{_sysconfdir}/profile.d/modules.csh
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/module.fish
%dir %{_datadir}/fish/vendor_functions.d/
%{_datadir}/fish/vendor_functions.d/module.fish

%files doc
%defattr(-,root,root)
%doc doc_dir/COPYING.GPLv2 doc_dir/ChangeLog doc_dir/ChangeLog-compat doc_dir/INSTALL.txt doc_dir/example.txt
%doc doc_dir/MIGRATING.txt doc_dir/NEWS-compat doc_dir/NEWS.txt doc_dir/README doc_dir/diff_v3_v4.txt

%changelog
