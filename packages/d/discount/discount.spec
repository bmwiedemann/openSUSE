#
# spec file for package discount
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


%define sover 2
%bcond_with fenced_code
Name:           discount
Version:        2.2.7b
Release:        0
Summary:        Markdown text to HTML converter
License:        BSD-3-Clause
Group:          Productivity/Text/Convertors
URL:            https://www.pell.portland.or.us/~orc/Code/discount/
Source:         https://www.pell.portland.or.us/~orc/Code/discount/discount-%{version}.tar.bz2
Patch1:         discount-disable_ldconfig.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
Provides:       markdown

%description
Discount is an implementation of John Gruber’s Markdown text to HTML language
with some extensions from PHP Markdown Extra, Pandoc, and other implementations
of Markdown.

%package -n libmarkdown%{sover}
Summary:        Markdown text to HTML converter library
Group:          Development/Libraries/C and C++

%description -n libmarkdown%{sover}
Discount is an implementation of John Gruber’s Markdown text to HTML language
with some extensions from PHP Markdown Extra, Pandoc, and other implementations
of Markdown.

%package -n libmarkdown-devel
Summary:        Markdown text to HTML converter library
Group:          Development/Libraries/C and C++
Requires:       libmarkdown%{sover} = %{version}

%description -n libmarkdown-devel
Discount is an implementation of John Gruber’s Markdown text to HTML language
with some extensions from PHP Markdown Extra, Pandoc, and other implementations
of Markdown.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags}" ./configure.sh \
  --shared \
  --prefix="%{_prefix}" \
  --execdir="%{_bindir}" \
  --confdir="%{_sysconfdir}" \
  --libdir="%{_libdir}" \
  --mandir="%{_mandir}" \
%if %{with fenced_code}
  --with-fenced-code \
%endif
  --with-dl=BOTH \
  --pkg-config \
  --enable-all-features
%make_build

%install
make DESTDIR=%{buildroot} install.everything

%fdupes -s %{buildroot}%{_mandir}/man3
install -D -p -m 0644 libmarkdown.pc \
  %{buildroot}%{_libdir}/pkgconfig/libmarkdown.pc

# update-alternatives
mv %{buildroot}%{_bindir}/markdown %{buildroot}%{_bindir}/discount-markdown
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/markdown
ln -sf %{_sysconfdir}/alternatives/markdown %{buildroot}%{_bindir}/markdown

%post
update-alternatives \
	--install %{_bindir}/markdown markdown %{_bindir}/discount-markdown 20

%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove markdown %{_bindir}/discount-markdown
fi

%post   -n libmarkdown%{sover} -p /sbin/ldconfig
%postun -n libmarkdown%{sover} -p /sbin/ldconfig

%files
%license COPYRIGHT
%doc CREDITS README
%{_bindir}/makepage
%{_bindir}/markdown
%{_bindir}/discount-markdown
%ghost %{_sysconfdir}/alternatives/markdown
%{_bindir}/mkd2html
%{_bindir}/theme
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man7/markdown.7%{?ext_man}
%{_mandir}/man7/mkd-extensions.7%{?ext_man}

%files -n libmarkdown%{sover}
%{_libdir}/libmarkdown.so.%{sover}*

%files -n libmarkdown-devel
%{_includedir}/mkdio.h
%{_libdir}/libmarkdown.so
%{_libdir}/pkgconfig/libmarkdown.pc
%{_mandir}/man3/*.3%{?ext_man}

%changelog
