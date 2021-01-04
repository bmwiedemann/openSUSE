#
# spec file for package myquerytutor
#
# Copyright (c) 2020 Steven Tucker <tuxta2@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiativ

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           myquerytutor
Version:        2.1.1+git20201224.0172df6
Release:        0
Summary:        Educational tool to teach SQL
License:        GPL-3.0
URL:            https://github.com/tuxta/myquerytutor
SOURCE0:        %{name}-%{version}.tar.xz
SOURCE1:        mqt.png
SOURCE2:        %{name}.desktop

%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  python3-PyQt5
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-devel
BuildRequires:  python3-qtwebengine-qt5
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files

Requires:       python3-PyQt5
Requires:       python3-beautifulsoup4
Requires:       python3-qtwebengine-qt5
Requires:       python3-requests
%endif

%if 0%{?fedora_version} == 33
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-qt5
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-qt5-webengine
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils

Requires:  python3-qt5
Requires:  python3-beautifulsoup4
Requires:  python3-qt5-webengine
Requires:  python3-requests
%endif

%if 0%{?arch_linux} 
BuildRequires:  git
BuildRequires:  python3
BuildRequires:  python-pyqt5
BuildRequires:  python-beautifulsoup4
BuildRequires:  python-pyqtwebengine
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  desktop-file-utils

Requires:  python3
Requires:  python-pyqt5
Requires:  python-beautifulsoup4
Requires:  python-pyqtwebengine
Requires:  python-requests
%endif

BuildArch:      noarch

%description
A personal tutor to teach you Structured Query Language.

%prep
%autosetup -p1
cp %{S:1} %{S:2} .

%if 0%{?fedora_version}
%setup
cp -p %{SOURCE1} mqt.png
cp -p %{SOURCE2} %{name}.desktop
%endif

%build
export LC_ALL=en_US.utf8

%if 0%{?suse_version}
%python3_build
%endif

%if 0%{?fedora_version}
%py3_build
%endif

%install
export LC_ALL=en_US.utf8
%if 0%{?suse_version}
%python3_install
%endif

%if 0%{?fedora_version}
%py3_install
%endif

%if 0%{?suse_version}
%suse_update_desktop_file -i myquerytutor
%endif

%if 0%{?fedora_version}
desktop-file-install --delete-original --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
mkdir -p %{buildroot}/usr/share/pixmaps
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps
%endif
   
rm -f %{buildroot}%{python3_sitelib}/main.py
rm -f %{buildroot}%{python3_sitelib}/__pycache__/*main*

%if 0%{?suse_version}
%python_expand %fdupes %{buildroot}%{python3_sitelib}/
%endif



%files
%license LICENSE
%{_bindir}/myquerytutor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/mqt.png
%{python3_sitelib}/



%changelog
