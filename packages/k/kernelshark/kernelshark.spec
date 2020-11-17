#
# spec file for package kernelshark
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
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/

Name:           kernelshark
Version:        1.2
Release:        0
Summary:        Visualisation tool for trace-cmd data
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Tools/Debuggers
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git
Source0:        kernelshark-%{version}.tar.xz
Source1:        kernelshark-rpmlintrc
Patch1:         makefile-lib64.patch
Patch2:         makefile-bash.patch
Patch3:         0001-trace-cmd-fix-multiple-definition-compiler-errors.patch
Patch4:         kernelshark-make-fontheight.patch
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  freeglut-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  python-devel
BuildRequires:  swig
Recommends:     trace-cmd
%if 0%{?suse_version} > 1200
BuildRequires:  xsltproc
%else
BuildRequires:  libxslt
%endif

%description
trace-cmd reporting can be extremely verbose making it difficult to
analyse. kernelshark visualises the data so that it can be filtered
or trimmed.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
make %{?_smp_mflags} prefix=%{_prefix} trace-cmd
make %{?_smp_mflags} prefix=%{_prefix} gui
make %{?_smp_mflags} MANPAGE_DOCBOOK_XSL=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl doc

%install
%make_install prefix=%{_prefix} install_gui
%make_install prefix=%{_prefix} install_doc
rm %{buildroot}/%{_mandir}/man1/trace-cmd*
rm %{buildroot}/%{_mandir}/man5/trace-cmd.dat.5
rm %{buildroot}/%{_datadir}/bash-completion/completions/trace-cmd.bash
rm -rf %{buildroot}/%{_libdir}/trace-cmd
rm -rf %{buildroot}/%{_bindir}/trace-cmd
rm -rf %{buildroot}/%{_datadir}/polkit-1
sed -i -e 's/^Categories=.*/Categories=Development;Profiling/' %{buildroot}/%{_datadir}/applications/kernelshark.desktop
sed -i -e 's/^Version=1.0.0/Version=1.0/' %{buildroot}/%{_datadir}/applications/kernelshark.desktop

%files
%{_mandir}/man1/kernelshark.1%{?ext_man}
%{_bindir}/kernelshark
%{_bindir}/kshark-*
%{_libdir}/kernelshark
%{_libdir}/libkshark*
%{_datadir}/applications/kernelshark.desktop
%{_datadir}/kernelshark
%{_datadir}/icons/kernelshark
%license COPYING

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
