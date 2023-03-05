#
# spec file for package yast2-devtools
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


Name:           yast2-devtools
Version:        4.6.0
Release:        0
Summary:        YaST2 - Development Tools
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-devtools
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  perl-XML-Writer
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
Requires:       yast2-buildtools
BuildArch:      noarch

%description
Scripts and templates for developing YaST2 modules and components.

%package -n yast2-buildtools
Summary:        Minimal set of tools needed to build yast module
# we install our .pc under $prefix/share
Requires:       autoconf
Requires:       automake
Requires:       gettext-tools
Requires:       perl
Requires:       perl-XML-Writer
Requires:       pkgconfig >= 0.16
Recommends:     cmake
# /usr/lib/YaST2/bin/ydoxygen needs it
Recommends:     doxygen
# for svn builds of binary packages
Recommends:     libtool
# for extracting translatable strings from *.rb files using "make pot" command
# weak dependency, "make pot" is usually not needed
Suggests:       rubygem(gettext)

%description -n yast2-buildtools
Scripts and templates required for rebuilding the existing YaST2
modules and components (both ruby and C++).

%prep
%setup -q

%build
make -f Makefile.cvs all

%configure
%make_build

%install
%make_install
[ -e "%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK" ] || Y2DIR="%{buildroot}%{_datadir}/YaST2" make check DESTDIR=%{buildroot}
for f in `find %{buildroot}%{_datadir}/applications/YaST2 -name "*.desktop"` ; do
    d=${f##*/}
    %suse_update_desktop_file -d ycc_${d%.desktop} ${d%.desktop}
done

%if 0%{?qemu_user_space_build}
# disable testsuite on QEMU builds, will fail
cat > "%{buildroot}%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK" <<EOF
Disabling testsuite on QEMU builds, as the userspace emulation
is not complete enough for yast2-core
EOF
%endif

# Change false to true in the following line when yast2 core is broken
false && cat > "%{buildroot}%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK" <<EOF
When yast2 core is broken and the interpreter does not work,
submitting yast2-devtools with the flag file existing will
prevent ycp developers being flooded by testsuite failures.
EOF

%fdupes %{buildroot}%{_prefix}

%files
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*ycp-mode.el
%dir %{_datadir}/vim
%dir %{_datadir}/vim/site
%dir %{_datadir}/vim/site/syntax
%{_datadir}/vim/site/syntax/ycp.vim
%dir %{_datadir}/vim/site/ftdetect
%{_datadir}/vim/site/ftdetect/ycp_filetype.vim
%dir %{_prefix}/lib/YaST2
%{_datadir}/cmake
%dir %{_datadir}/YaST2
%doc %{_docdir}/%{name}
%dir %{_prefix}/lib/YaST2/bin
%{_prefix}/lib/YaST2/bin/scrdoc
%{_prefix}/lib/YaST2/bin/ycp_puttext
%{_prefix}/lib/YaST2/bin/ydoxygen
%dir %{_datadir}/YaST2/clients/
%{_datadir}/YaST2/clients/ycp2yml.rb
%{_datadir}/YaST2/data/devtools/bin/check-textdomain
%{_datadir}/YaST2/data/devtools/bin/check_icons
%{_datadir}/YaST2/data/devtools/bin/create_maintenance_branch
%{_datadir}/YaST2/data/devtools/bin/find-unused-published
%{_datadir}/YaST2/data/devtools/bin/get-lib
%{_datadir}/YaST2/data/devtools/bin/pot-spellcheck
%{_datadir}/YaST2/data/devtools/bin/rny2rnc
%{_datadir}/YaST2/data/devtools/bin/showy2log
%{_datadir}/YaST2/data/devtools/bin/tagversion
%{_datadir}/YaST2/data/devtools/bin/y2makepot
%{_datadir}/YaST2/data/devtools/bin/po_add_format_hints
%{_datadir}/YaST2/data/devtools/bin/gettextdomains
%{_datadir}/YaST2/data/devtools/bin/ycp_puttext
%{_datadir}/YaST2/data/devtools/data/rubocop*_yast_style.yml
%dir %{_datadir}/YaST2/control/
%{_datadir}/YaST2/control/yast_control.its
%{_datadir}/YaST2/control/qt_ui.its

%files -n yast2-buildtools
%{_rpmmacrodir}/macros.yast
%{_bindir}/y2tool
%{_datadir}/aclocal/*.m4
%{_datadir}/pkgconfig/yast2-devtools.pc
%{_datadir}/YaST2/data/docbook
%dir %{_datadir}/YaST2/data
%dir %{_datadir}/YaST2/data/devtools
%dir %{_datadir}/YaST2/data/devtools/bin
%{_datadir}/YaST2/data/devtools/admin
%{_datadir}/YaST2/data/devtools/Doxyfile
%if 0%{?qemu_user_space_build}
%{_datadir}/YaST2/data/devtools/NO_MAKE_CHECK
%endif
# needed for doxygen, not nice
%{_datadir}/YaST2/data/devtools/footer-notimestamp.html
%dir %{_datadir}/YaST2/data/devtools/data
%{_datadir}/YaST2/data/devtools/data/YaST2.dict.txt
%{_datadir}/YaST2/data/devtools/bin/y2autoconf
%{_datadir}/YaST2/data/devtools/bin/y2automake
%{_datadir}/YaST2/data/devtools/bin/y2metainfo
%license COPYING

%changelog
