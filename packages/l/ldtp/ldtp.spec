#
# spec file for package ldtp
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ldtp
Version:        3.5.0
Release:        0
Summary:        Linux Desktop Testing Project (LDTP)
License:        LGPL-2.1
Group:          Productivity/Other
Url:            http://ldtp.freedesktop.org
Source:         http://download.freedesktop.org/ldtp/3.x/3.5.x/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
%if !(0%{?favor_gtk2})
BuildRequires:  gobject-introspection
%endif
BuildRequires:  python
# pyatspi is a virtual name that is provided by the default at-spi stack
Requires:       pyatspi
%if 0%{?favor_gtk2}
%if 0%{?suse_version} <= 1130
Requires:       gnome-python-desktop
%else
Requires:       python-wnck
%endif
Requires:       python-gtk
%endif
Requires:       python-twisted-web
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{suse_version} > 1110
BuildArch:      noarch
%endif
%py_requires
%if %suse_version <= 1110
%define python_sitelib %{py_sitedir}
%endif

%description
The GNU/Linux Desktop Testing Project (GNU LDTP) aims to produce a
high quality test automation framework with cutting-edge tools that
can be used to test and improve the GNU/Linux or Solaris desktops.
It uses the Accessibility libraries to discover through the
application's user interface. The framework also has tools to
record test-cases based on user actions in an application.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%fdupes %{buildroot}/%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS README COPYING
%{_bindir}/ldtp
%{python_sitelib}/ldtp/
%{python_sitelib}/ldtpd/
%{python_sitelib}/ldtputils/
%{python_sitelib}/ooldtp/
%{python_sitelib}/ldtp-%{version}-*.egg-info

%changelog
