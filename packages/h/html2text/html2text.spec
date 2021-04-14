#
# spec file for package html2text
#
# Copyright (c) 2021 SUSE LLC
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


Name:           html2text
Version:        2.0.0
Release:        0
Summary:        HTML to ASCII Converter
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/HTML/Tools
URL:            https://github.com/grobian/html2text
Source0:        https://github.com/grobian/html2text/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        html2text.1.gz
BuildRequires:  gcc-c++
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description
A tool for converting from HTML to ASCII. It can reasonably handle
tables.

%prep
%autosetup

%build
%configure
%make_build EXPLICIT="%{optflags}"

%install
# To avoid conflicts with the python3-html2text package
install -Dpm 0755 html2text \
  %{buildroot}%{_bindir}/html2text-cpp
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_mandir}/man1/html2text-cpp.1.gz
gzip html2textrc.5
install -Dpm 0644 html2textrc.5.gz \
  %{buildroot}%{_mandir}/man5/html2textrc.5.gz

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
%license COPYING
%doc CHANGES TODO CREDITS KNOWN_BUGS RELEASE_NOTES
%{_bindir}/html2text
%{_bindir}/html2text-cpp
%ghost %{_sysconfdir}/alternatives/html2text
%{_mandir}/man1/html2text.1%{?ext_man}
%{_mandir}/man1/html2text-cpp.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/html2text.1.gz
%{_mandir}/man5/html2textrc.5%{?ext_man}

%changelog
