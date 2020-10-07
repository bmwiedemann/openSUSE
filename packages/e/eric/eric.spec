#
# spec file for package eric
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2010 LISA GmbH, Bingen, Germany
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


%define distname eric6

Name:           eric
Version:        20.10
Release:        0
Summary:        Python IDE based on Qt5
License:        GPL-3.0-or-later
Group:          Development/Tools/IDE
URL:            https://eric-ide.python-projects.org/
Source:         https://sourceforge.net/projects/eric-ide/files/%{distname}/stable/%{version}/%{distname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-qscintilla-qt5
BuildRequires:  python3-qt5
BuildRequires:  python3-qtcharts-qt5
BuildRequires:  python3-qtwebengine-qt5
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
Requires:       python3-qscintilla-qt5
Requires:       python3-qt5
Requires:       python3-qtcharts-qt5
Requires:       python3-qtwebengine-qt5
Requires:       python3-xml
Recommends:     %{name}-api = %{version}
Recommends:     python3-Markdown
Recommends:     python3-cx_Freeze
Recommends:     python3-doc
Recommends:     python3-enchant >= 1.5.3
Recommends:     python3-pylint >= 0.18.0
Recommends:     python3-pysvn >= 1.7.0
Recommends:     python3-rope >= 0.9.2
Provides:       python-eric5 = %{version}
Obsoletes:      python-eric5 < %{version}
Provides:       python-eric6 = %{version}
Obsoletes:      python-eric6 < %{version}
Provides:       eric5 = %{version}
Obsoletes:      eric5 < %{version}
Provides:       eric6 = %{version}
Obsoletes:      eric6 < %{version}
BuildArch:      noarch

%description
Eric is a Python and Ruby editor and IDE, written in Python. It is
based on the Qt GUI toolkit and integrates the Scintilla editor
control.

%package api
Summary:        API files for eric6
Group:          Development/Tools/IDE
Provides:       python-eric5-api = %{version}
Obsoletes:      python-eric5-api < %{version}
Provides:       python-eric6-api = %{version}
Obsoletes:      python-eric6-api < %{version}
Provides:       eric5-api = %{version}
Obsoletes:      eric5-api < %{version}
Provides:       eric6-api = %{version}
Obsoletes:      eric6-api < %{version}

%description api
This package provides API files for eric6.
If both python-eric6 and python3-eric6 packages are installed then only one
python-eric6-api or python3-eric6-api is needed.

%prep
%setup -q -n %{distname}-%{version}

find . -name \*.py -exec sed -i -e '/^#!\/usr\/bin.*python/d' '{}' \;

%build
# nothing here

%install
python3 install.py -b %{_bindir} -d %{python3_sitelib} -i %{buildroot}
%fdupes %{buildroot}%{python3_sitelib}
ln -sf eric6 %{buildroot}%{_bindir}/%{name}

%files
%license eric/docs/LICENSE.GPL3
%doc eric/docs/README*.rst eric/docs/THANKS eric/docs/eric6-plugin.odt
%{_bindir}/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{distname}.appdata.xml
%{_datadir}/applications/%{distname}.desktop
%{_datadir}/applications/%{distname}_browser.desktop
%{_datadir}/pixmaps/eric.png
%{_datadir}/pixmaps/ericWeb.png
%{python3_sitelib}/

%files api
%license eric/docs/LICENSE.GPL3
%dir %{_datadir}/qt5
%dir %{_datadir}/qt5/qsci/api/python
%{_datadir}/qt5/qsci/api/python/*
%dir %{_datadir}/qt5/qsci/api/ruby
%{_datadir}/qt5/qsci/api/ruby/*
%dir %{_datadir}/qt5/qsci/api/qss
%{_datadir}/qt5/qsci/api/qss/*

%changelog
