#
# spec file for package mcomix
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mcomix
Version:        1.2.1
Release:        0
Summary:        Comics Viewer
License:        GPL-2.0-only
Group:          Productivity/Graphics/Viewers
Url:            http://sourceforge.net/p/mcomix/wiki/Home/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         python-pillow-fix-attributeerror.patch
# not Python3 ready :(
BuildRequires:  python-setuptools
Requires:       python-Pillow
Requires:       python-gtk
Requires:       python-setuptools
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     unrar
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
Comics Viewer forked from comix.

%prep
%setup -q
%patch0 -p1

%build

%install
python setup.py install --root %{buildroot} --prefix "%{_prefix}"
{
	echo '%defattr(-,root,root,-)'
	ls %{buildroot}%{python_sitelib}/mcomix/messages/*/LC_MESSAGES/mcomix.mo | \
	sed 's@%{buildroot}\(%{python_sitelib}/mcomix/messages/\([^/]\+\)/LC_MESSAGES/mcomix.mo\)@%lang(\2) \1@'
} | tee %{name}.lang

%if 0%{?suse_version}
%fdupes -s %{buildroot}%{_datadir}/icons
%fdupes -s %{buildroot}%{python_sitelib}/mcomix
%fdupes -s %{buildroot}%{python_sitelib}/mcomix-*
%endif

%post
%mime_database_post

%postun
%mime_database_postun

%files -f %{name}.lang
%doc
%{_bindir}/mcomix
%{python_sitelib}/mcomix-*
%dir %{python_sitelib}/mcomix/
%{python_sitelib}/mcomix/*.py*
%{python_sitelib}/mcomix/library/
%{python_sitelib}/mcomix/images/
%{python_sitelib}/mcomix/archive/
%{python_sitelib}/mcomix/win32/
# only directories and python, rest is in lang file
%dir %{python_sitelib}/mcomix/messages/
%dir %{python_sitelib}/mcomix/messages/*
%dir %{python_sitelib}/mcomix/messages/*/LC_MESSAGES
%{python_sitelib}/mcomix/messages/__init__.py*
%{_datadir}/appdata
%{_datadir}/applications/mcomix.desktop
%{_datadir}/icons/hicolor
%{_datadir}/mime/packages/mcomix.xml
%{_mandir}/man1/mcomix*

%changelog
