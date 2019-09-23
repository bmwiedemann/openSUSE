#
# spec file for package wxWidgets-docs (Version 2.8.11)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           wxWidgets-docs
Group:          System/Libraries
Url:            http://www.wxwidgets.org/
Summary:        wxWidgets Documentation
License:        GPL-2.0+
Version:        2.8.12
Release:        0
# %( exec >&2 ; cd %{_sourcedir} ; if ! test -f wxWidgets-%{version}-HTML.tar.bz2 ; then wget -N http://downloads.sourceforge.net/wxwindows/wxWidgets-%{version}-HTML.zip ; mkdir wxWidgets-HTML ; cd wxWidgets-HTML ; unzip ../wxWidgets-%{version}-HTML.zip ; tar -jcf ../wxWidgets-%{version}-HTML.tar.bz2 * ; cd .. ; rm -r wxWidgets-HTML ; fi )
Source:         wxWidgets-%{version}-HTML.tar.bz2
# %( exec >&2 ; cd %{_sourcedir} ; if ! test -f wxWidgets-%{version}-PDF.tar.bz2 ; then wget -N http://downloads.sourceforge.net/wxwindows/wxWidgets-%{version}-PDF.zip ; mkdir wxWidgets-PDF ; cd wxWidgets-PDF ; unzip ../wxWidgets-%{version}-PDF.zip ; tar -jcf ../wxWidgets-%{version}-PDF.tar.bz2 * ; cd .. ; rm -r wxWidgets-PDF ; fi )
Source1:        wxWidgets-%{version}-PDF.tar.bz2
Source2:        wxWidgets-docs-rpmlintrc
# Name up to 11.3 (was packaged together with wxPython documentation):
Provides:       wxGTK-doc = %{version}.0
Obsoletes:      wxGTK-doc < 2.8.11.0
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains wxWidgets documentation in HTML format.

%prep
%setup -q -T -c -a0 -a1

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/wxWidgets
cp -r * $RPM_BUILD_ROOT%{_docdir}/wxWidgets
%fdupes $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc %{_docdir}/wxWidgets

%changelog
