#
# spec file for package OpenLP
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


Name:           OpenLP
Version:        2.4.6
Release:        0
Summary:        Open source Church presentation and lyrics projection application
License:        GPL-2.0
Group:          Productivity/Multimedia/Other
Url:            http://openlp.org
Source0:        https://get.openlp.org/%{version}/%{name}-%{version}.tar.gz
Source1:        OpenLP-rpmlintrc
Patch0:         suse_corrections.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  libqt5-linguist
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       hicolor-icon-theme
Requires:       python3-Mako
Requires:       python3-SQLAlchemy
Requires:       python3-alembic
Requires:       python3-beautifulsoup4
Requires:       python3-chardet
Requires:       python3-lxml
Requires:       python3-nose
Requires:       python3-pyenchant
Requires:       python3-qt5
Requires:       python3-xdg
Recommends:     libreoffice-pyuno
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
BuildArch:      noarch

%description
OpenLP is a church presentation software, for lyrics projection software,
used to display slides of Songs, Bible verses, videos, images, and
presentations via LibreOffice using a computer and projector.

%prep
%setup -q
%patch0 -p1

# Remove unit tests
rm tests/__init__.py

%build
python3 setup.py build

# Compile the translation files and copy them to the correct directory
# Presumes you are in the base directory of OpenLP

%install
python3 setup.py install --skip-build -O1 --prefix=%{_prefix} --root=%{buildroot}

install -m644 -p -D resources/images/openlp-logo-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo-32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/openlp.png
install -m644 -p -D resources/images/openlp-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/openlp.svg

%suse_update_desktop_file -i -r openlp AudioVideo Video Player

mv %{buildroot}%{_bindir}/openlp.py %{buildroot}%{_bindir}/openlp

mkdir -p %{buildroot}%{_datadir}/openlp/i18n/
for TSFILE in resources/i18n/*.ts; do
    lrelease-qt5 $TSFILE -qm %{buildroot}%{_datadir}/openlp/i18n/`basename $TSFILE .ts`.qm;
done

mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p resources/openlp.xml %{buildroot}%{_datadir}/mime/packages

# Deduplicate .pyc and .pyo files
%fdupes %{buildroot}%{python_sitelib}

%post
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-mime-database %{_datadir}/mime > /dev/null 2>&1 ||:
update-desktop-database > /dev/null 2>&1 ||:

%postun
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-mime-database %{_datadir}/mime > /dev/null 2>&1 ||:
update-desktop-database > /dev/null 2>&1 ||:

%files
%defattr(-,root,root)
%doc copyright.txt LICENSE
%{_bindir}/openlp
%{_datadir}/mime/packages/openlp.xml
%{_datadir}/applications/openlp.desktop
%{_datadir}/icons/hicolor
%{_datadir}/openlp
%{python3_sitelib}/openlp/
%{python3_sitelib}/%{name}-%{version}*.egg-info

%changelog
