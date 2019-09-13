#
# spec file for package html2text
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           html2text
Version:        1.3.2a
Release:        0
Summary:        HTML to ASCII Converter
License:        GPL-2.0+
Group:          Productivity/Publishing/HTML/Tools
Url:            http://www.mbayer.de/html2text/
Source0:        http://www.mbayer.de/html2text/downloads/html2text-%{version}.tar.gz
Source1:        http://www.mbayer.de/html2text/html2text-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        html2text.1.gz
Patch0:         html2text-debian-200_close_files_inside_main_loop.patch
Patch1:         html2text-debian-220_nobs_when_stdout_is_a_tty.patch
Patch2:         html2text-1.3.2a-400_remove_builtin_http_support.patch
Patch3:         html2text-debian-500_utf8_support.patch
Patch4:         html2text-debian-510_disable_backspaces.patch
Patch5:         html2text-debian-600_multiple_meta_tags.patch
Patch6:         html2text-1.3.2a-611_recognize_input_encoding.patch
Patch7:         html2text-debian-630_recode_output_to_locale_charset.patch
Patch8:         http://www.mbayer.de/html2text/downloads/patch-amd64-html2text-1.3.2a.diff
Patch9:         html2text-debian-810_fix_deprecated_conversion_warnings.patch
BuildRequires:  gcc-c++
Requires(post):   update-alternatives
Requires(preun):  update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A tool for converting from HTML to ASCII. It can reasonably handle
tables.

%prep
%setup -q
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
cp -a %{SOURCE3} .

%build
%configure
make %{?_smp_mflags} EXPLICIT="%{optflags}"

%install
# To avoid conflicts with the python3-html2text package
install -D -m 0755 html2text        %{buildroot}%{_bindir}/html2text-cpp
install -D -m 0644 html2text.1.gz   %{buildroot}%{_mandir}/man1/html2text-cpp.1.gz
install -D -m 0644 html2textrc.5.gz %{buildroot}%{_mandir}/man5/html2textrc.5.gz

ln -s -f %{_sysconfdir}/alternatives/html2text %{buildroot}%{_bindir}/html2text
ln -s -f %{_sysconfdir}/alternatives/html2text.1.gz %{buildroot}%{_mandir}/man1/html2text.1.gz

%post
update-alternatives --install %{_bindir}/html2text html2text %{_bindir}/html2text-cpp 30 \
                    --slave %{_mandir}/man1/html2text.1.gz html2text.1.gz %{_mandir}/man1/html2text-cpp.1.gz

%preun
if [ ! -f %{_bindir}/html2text-cpp ] ; then
   update-alternatives --remove html2text %{_bindir}/html2text-cpp
fi

%files
%defattr(-,root,root)
%doc README CHANGES COPYING TODO CREDITS KNOWN_BUGS RELEASE_NOTES
%{_bindir}/html2text
%{_bindir}/html2text-cpp
%ghost %{_sysconfdir}/alternatives/html2text
%{_mandir}/man1/html2text.1.gz
%{_mandir}/man1/html2text-cpp.1.gz
%ghost %{_sysconfdir}/alternatives/html2text.1.gz
%{_mandir}/man5/html2textrc.5.gz

%changelog
