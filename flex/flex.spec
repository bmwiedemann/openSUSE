#
# spec file for package flex
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


%define somajor 2
Name:           flex
Version:        2.6.4
Release:        0
Summary:        Fast Lexical Analyzer Generator
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Url:            http://flex.sourceforge.net/
Source:         https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz
Source1:        lex-wrapper.sh
Source2:        README.SUSE
Source3:        baselibs.conf
Patch:          use-extensions.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  m4
Requires:       libfl-devel = %{version}
Requires:       m4
Requires(post): %{install_info_prereq}
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FLEX is a tool for generating scanners: programs that recognize lexical
patterns in text.

%package -n libfl-devel
Summary:        Development files for flex
Group:          Development/Languages/C and C++
Requires:       libfl%{somajor} = %{version}

%description -n libfl-devel
FLEX is a tool for generating scanners: programs that recognize lexical
patterns in text.

This package contains files required to build programs with flex libraries.

%package -n libfl%{somajor}
Summary:        Libraries for flex
Group:          System/Libraries

%description -n libfl%{somajor}
FLEX is a tool for generating scanners: programs that recognize lexical
patterns in text.

This package contains libraries for using flex.

%prep
%setup -q
%patch -p1

%build
autoreconf -fi
%configure \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%check
%if !0%{?qemu_user_space_build:1}
make %{?_smp_mflags} check
%endif

%install
%make_install
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
install -D -p -m 0755 %{SOURCE1}  %{buildroot}/%{_bindir}/lex
install -D -p -m 0644 %{SOURCE2}  %{buildroot}/%{_docdir}/flex/README.SUSE
ln -s flex.1%{ext_man} %{buildroot}/%{_mandir}/man1/lex.1%{ext_man}

%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%post   -n libfl%{somajor} -p /sbin/ldconfig
%postun -n libfl%{somajor} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS ONEWS README.md THANKS
%{_bindir}/flex
%{_bindir}/flex++
%{_bindir}/lex
%{_mandir}/man1/flex.1%{ext_man}
%{_mandir}/man1/lex.1%{ext_man}
%{_infodir}/flex*
%{_docdir}/%{name}

%files -n libfl-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS ONEWS README.md THANKS
%{_includedir}/FlexLexer.h
%{_libdir}/libfl.so

%files -n libfl%{somajor}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS ONEWS README.md THANKS
%{_libdir}/libfl.so.%{somajor}*

%changelog
