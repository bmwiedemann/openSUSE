#
# spec file for package git-cola
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Marcin Bajor
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


Name:           git-cola
Version:        3.7
Release:        0
Summary:        A GUI for Git
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://git-cola.github.io/

%{!?python_sitelib: %global python_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Source:         https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dos2unix
BuildRequires:  git-core
BuildRequires:  python3
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  python3-pyinotify
BuildRequires:  python3-qt5
BuildRequires:  update-desktop-files
Requires:       git-core
Requires:       python3-qt5
Recommends:     python3-pyinotify
Recommends:     gitk
Recommends:     python3-Send2Trash

%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description
git-cola is a graphical user interface for Git that provides a way to
interact with Git repositories.

%prep
%setup -q

%build
dos2unix qtpy/py3compat.py

%install
%makeinstall prefix=%{_prefix} DESTDIR=%{buildroot} PYLINT=pylint3 PYTHON=python3 PIP=pip3

make install-man prefix=%{_prefix} DESTDIR=%{buildroot}  PYLINT=pylint3 PYTHON=python3 PIP=pip3

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/git-cola.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/git-dag.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/git-cola-folder-handler.desktop

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/cola
%{_bindir}/git-cola
%{_bindir}/git-dag
%dir %{_datadir}/git-cola
%{_datadir}/git-cola/*
%{_datadir}/applications/git-cola.desktop
%{_datadir}/applications/git-dag.desktop
%{_datadir}/applications/git-cola-folder-handler.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/git-cola.svg
%dir %{_datadir}/doc/git-cola
%{_datadir}/doc/git-cola/*
%if 0%{?sles_version} > 9
%{_datadir}/locale/zh_cn
%endif
%dir %{_datadir}/appdata/
%{_datadir}/appdata/git-cola.appdata.xml
%{_datadir}/appdata/git-dag.appdata.xml
%{_mandir}/man1/*.*

%changelog
