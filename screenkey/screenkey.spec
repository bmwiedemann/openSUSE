#
# spec file for package screenkey
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           screenkey
Version:        0.9
Release:        0
Summary:        A screen-cast tool to show keys
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
URL:            https://www.thregr.org/~wavexx/software/screenkey/
Source0:        https://github.com/wavexx/screenkey/archive/screenkey-%{version}.tar.gz
Patch0:         screenkey_icon.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python-devel
BuildRequires:  python2-distutils-extra
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools-git
Requires:       python
Requires:       python2-cairo
Requires:       python-gtk
Requires:       slop
Recommends:     fontawesome-fonts
Recommends:     python2-appindicator
BuildArch:      noarch

%description
A screencast tool to show keys. Inspired by Screenflick and based on
the key-mon project.

%prep
%setup -q -n screenkey-screenkey-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}" python setup.py build

%install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}
find build/lib* -name '*.py' -exec sed -i "1{/^#!/d}" {} + && \
python setup.py install -O1 --skip-build --root %{buildroot} --prefix %{_prefix}/
%fdupes -s %{buildroot}

%files
%{_bindir}/screenkey
%{_datadir}/applications/screenkey.desktop
%{python_sitelib}/Screenkey
%{python_sitelib}/screenkey-%{version}-py2.7.egg-info
%doc %{_datadir}/doc/screenkey/

%changelog
