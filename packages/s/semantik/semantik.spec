#
# spec file for package semantik
#
# Copyright (c) 2024 SUSE LLC
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


Name:           semantik
Version:        1.2.10
Release:        0
Summary:        A mindmapping-like tool
License:        GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://waf.io/semantik.html
Source0:        https://waf.io/%{name}-%{version}.tar.bz2
Source1:        %{name}.1
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kdelibs4support-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtwebengine-devel
BuildRequires:  python3-Pygments
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1500
BuildRequires:  rpm_macro(_kf5_kxmlguidir)
%else
BuildRequires:  kf5-filesystem
%endif

%description
Semantik (previously Kdissert) is a mindmapping-like tool to help students
to produce complicated documents very quickly and efficiently :
presentations, dissertations, thesis, reports.

While targetted mostly at students, Semantik can also help teachers,
decision maker, engineers and businessmen.

Though this application shares some similarities with general-purpose
mindmapping tools like Freemind or Vym, the very first goal of Semantik is
to create general-purpose documents through the use of mindmaps.

%prep
%setup -q

#wrong-icon-size
convert -strip src/data/hi48-app-semantik-d.png -resize 48x48 src/data/hi48-app-semantik-d.png
#env-script-interpreter
for i in src/filters/*.py src/sembind.py waf; do
  sed -i '1s:.*:#!/usr/bin/python3:' $i;
done

%build

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

./waf configure \
      --prefix=%{_prefix} \
      --python=%{_bindir}/python3

./waf build %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}
install -Dm0644 src/data/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
install -m0644 src/data/%{name}-d.svg %{buildroot}%{_datadir}/pixmaps/%{name}-d.svg
%suse_update_desktop_file -i %{name} Office ProjectManagement
%suse_update_desktop_file -i %{name}-d Office ProjectManagement
%find_lang %{name} --all-name
%fdupes %{buildroot}

# fix non-executable-script
chmod a+rx %{buildroot}%{_datadir}/semantik/templates/pdflatex/wscript
chmod a+rx %{buildroot}%{_datadir}/semantik/templates/beamer/wscript
chmod a+rx %{buildroot}%{_datadir}/semantik/templates/waf
chmod a+rx %{buildroot}%{_datadir}/semantik/filters/*.py
chmod a+rx %{buildroot}%{_datadir}/semantik/sembind.py

# fix the script interpreter
sed -i -e 's|#! /usr/bin/python|#!/usr/bin/python3|' %{buildroot}%{_datadir}/semantik/templates/pdflatex/wscript
sed -i -e 's|#! /usr/bin/python|#!/usr/bin/python3|' %{buildroot}%{_datadir}/semantik/templates/beamer/wscript

# install man page
install -D -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license LICENSE
%doc ChangeLog README
%{_bindir}/semantik*
%{_libdir}/lib*.so*
%{_datadir}/applications/semantik*.desktop
%{_datadir}/pixmaps/*.svg
%{_datadir}/icons/hicolor/*/apps/semantik*.svg
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*
%{_datadir}/semantik
%{_kf5_kxmlguidir}/semantik*

%changelog
