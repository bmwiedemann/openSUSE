#
# spec file for package mcomix
#
# Copyright (c) 2023 SUSE LLC
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


%{?sle15_python_module_pythons}

%if 0%{?suse_version} > 1500
%define pythons python3
%endif
%if 0%{?sle_version} == 0150400
%define pythons python310
%endif

Name:           mcomix
Version:        2.3.0
Release:        0
Summary:        Comics Viewer
License:        GPL-2.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://sourceforge.net/p/mcomix/wiki/Home/
Source0:        https://sourceforge.net/projects/mcomix/files/MComix-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gobject-introspection
%if 0%{?suse_version} > 1500
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-Pillow
Requires:       python3-PyMuPDF
Requires:       python3-gobject-Gdk
Requires:       python3-pycairo
%endif
%if 0%{?sle_version} >= 0150500
BuildRequires:  python311-devel
BuildRequires:  python311-setuptools
Requires:       mupdf
Requires:       python311-Pillow
Requires:       python311-gobject-Gdk
Requires:       python311-pycairo
%endif
%if 0%{?sle_version} == 0150400
BuildRequires:  python310-devel
BuildRequires:  python310-setuptools
Requires:       mupdf
Requires:       python310-Pillow
Requires:       python310-gobject-Gdk
Requires:       python310-pycairo
%endif
Requires:       /usr/bin/7z
Requires:       python3-chardet
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

%install
%python_exec setup.py install --single-version-externally-managed --root %{buildroot} --prefix "%{_prefix}"
{
	echo '%defattr(-,root,root,-)'
	%{python_expand ls %{buildroot}%{$python_sitelib}/mcomix/messages/*/LC_MESSAGES/mcomix.mo | \
	sed 's@%{buildroot}\(%{$python_sitelib}/mcomix/messages/\([^/]\+\)/LC_MESSAGES/mcomix.mo\)@%lang(\2) \1@' }
} | tee %{name}.lang

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
# only directories and python, rest is in lang file
%dir %{python_sitelib}/mcomix/messages/
%dir %{python_sitelib}/mcomix/messages/*
%dir %{python_sitelib}/mcomix/messages/*/LC_MESSAGES
%{_datadir}/appdata/*
%{_datadir}/applications/mcomix.desktop
%{_datadir}/icons/hicolor
%{_datadir}/mime/packages/mcomix.xml
%{_mandir}/man1/mcomix*

%changelog
