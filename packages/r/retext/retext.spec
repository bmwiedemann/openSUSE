#
# spec file for package retext
#
# Copyright (c) 2020 SUSE LLC
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


Name:           retext
Version:        7.1.0
Release:        0
Summary:        Simple editor for Markdown and reStructuredText
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/retext-project/retext
Source:         https://github.com/retext-project/retext/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3
BuildRequires:  python3-Markdown
BuildRequires:  python3-Markups >= 2.0
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-qt5
BuildRequires:  python3-setuptools
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
Requires:       python3-Markdown
Requires:       python3-Markups >= 2.0
Requires:       python3-docutils
Requires:       python3-pyenchant
Requires:       python3-qt5
Recommends:     python3-Pygments
Provides:       ReText = %{version}
BuildArch:      noarch

%description
ReText is simple text editor that supports Markdown and reStructuredText
markup languages. It is written in Python using PyQt libraries.

%prep
%autosetup
dos2unix LICENSE_GPL
# remove shebang
sed -i '/^#!/d' ReText/__main__.py ReText/converterprocess.py

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}

mkdir -pv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -pv %{buildroot}%{_datadir}/%{name}/
mkdir -pv %{buildroot}%{_datadir}/applications/

cp -r icons/*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ICONSIZE="16 22 32 48 64 128 256"
pushd %{buildroot}%{_datadir}/icons/hicolor/
for i in $ICONSIZE; do
  mkdir -pv ${i}x${i}/apps/
  rsvg-convert -h $i -w $i scalable/apps/%{name}.svg -o ${i}x${i}/apps/%{name}.png
done
popd

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/me.mitya57.ReText.desktop

%fdupes %{buildroot}%{_prefix}

%files
%doc changelog.md README.md configuration.md
%license LICENSE_GPL
%{_bindir}/%{name}
%{python3_sitelib}/ReText/
%{python3_sitelib}/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*appdata.xml

%changelog
