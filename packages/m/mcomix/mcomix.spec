#
# spec file for package mcomix
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} >= 1600
%define pythons python3
%else
%define pythons python311
%endif

Name:           mcomix
Version:        3.1.0
Release:        0
Summary:        Comics Viewer
License:        GPL-2.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://sourceforge.net/p/mcomix/wiki/Home/
Source0:        https://sourceforge.net/projects/mcomix/files/MComix-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  gobject-introspection
%if 0%{?suse_version} > 1600
Requires:       python3-PyMuPDF
%else
Requires:       mupdf
%endif
Requires:       %{pythons}
Requires:       %{pythons}-Pillow
Requires:       %{pythons}-gobject-Gdk
Requires:       %{pythons}-pycairo
Requires:       /usr/bin/7z
Requires:       /usr/bin/chardetect
Requires:       typelib-1_0-Gtk-3_0
Recommends:     /usr/bin/lha
Recommends:     unrar
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
Comics Viewer forked from comix.

%prep
%setup -q
# remove extra executable flags
find . -type f | xargs chmod a-x

%build
%pyproject_wheel

%install
%pyproject_install
{
	echo '%defattr(-,root,root,-)'
	%{python_expand ls %{buildroot}%{$python_sitelib}/mcomix/messages/*/LC_MESSAGES/mcomix.mo | \
	sed 's@%{buildroot}\(%{$python_sitelib}/mcomix/messages/\([^/]\+\)/LC_MESSAGES/mcomix.mo\)@%lang(\2) \1@' }
} | tee %{name}.lang
install -Dm 644 share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
for a in share/icons/hicolor/* ; do
    install -Dm 644 -t %{buildroot}%{_datadir}/icons/hicolor/${a##*/}/apps $a/apps/*
    [[ -d $a/mimetypes ]] && install -Dm 644 -t %{buildroot}%{_datadir}/icons/hicolor/${a##*/}/mimetypes $a/mimetypes/*
done
install -Dm 644 share/mime/packages/%{name}.xml %{buildroot}%{_datadir}/mime/packages/%{name}.xml
install -Dm 644 share/metainfo/%{name}.metainfo.xml %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
install -Dm 644 share/man/man1/%{name}.1.gz -t %{buildroot}%{_datadir}/man/man1

%if 0%{?suse_version}
%fdupes -s %{buildroot}%{_datadir}/icons
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}/mcomix
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}/mcomix-*
%endif

%files -n %{name} -f %{name}.lang
%attr(755,root,root) %{_bindir}/mcomix
%{python_sitelib}/mcomix-*
%dir %{python_sitelib}/mcomix/
%{python_sitelib}/mcomix/*.py*
%{python_sitelib}/mcomix/library/
%{python_sitelib}/mcomix/images/
%{python_sitelib}/mcomix/messages/
%{python_sitelib}/mcomix/archive/
%{python_sitelib}/mcomix/__pycache__/
%{python_sitelib}/mcomix/_vendor/
%{_datadir}/metainfo/*
%{_datadir}/applications/mcomix.desktop
%{_datadir}/icons/hicolor
%{_datadir}/mime/packages/mcomix.xml
%{_mandir}/man1/mcomix*

%changelog
