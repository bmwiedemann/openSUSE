#
# spec file for package folder-color
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   folder_color
Name:           folder-color
Version:        0.0.79
Release:        0
Summary:        Change a directory colour in Caja and Nautilus
License:        GPL-3.0+
Group:          Productivity/File utilities
Url:            https://launchpad.net/folder-color
Source0:        http://archive.ubuntu.com/ubuntu/pool/universe/f/%{name}-common/%{name}-common_%{version}.orig.tar.gz
Source1:        http://archive.ubuntu.com/ubuntu/pool/universe/f/%{name}-caja/%{name}-caja_%{version}.orig.tar.gz
Source2:        http://archive.ubuntu.com/ubuntu/pool/universe/f/%{name}/%{name}_%{version}.orig.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python
BuildRequires:  python-distutils-extra
BuildArch:      noarch

%description
Change a directory colour, then get better visual layout.

%package -n caja-extension-%{name}
Summary:        Change a directory colour in Caja
Group:          Productivity/File utilities
Requires:       %{name}-common = %{version}
Requires:       caja
Requires:       python-caja
# folder-color-caja was last used in openSUSE Leap 42.1.
Provides:       %{name}-caja = %{version}
Obsoletes:      %{name}-caja < %{version}

%description -n caja-extension-%{name}
Change a directory colour, then get better visual layout.

%package -n nautilus-extension-%{name}
Summary:        Change a directory colour in Nautilus
Group:          Productivity/File utilities
Requires:       %{name}-common = %{version}
Requires:       nautilus
Requires:       python-nautilus
# folder-color-nautilus was last used in openSUSE Leap 42.1.
Provides:       %{name}-nautilus = %{version}
Obsoletes:      %{name}-nautilus < %{version}

%description -n nautilus-extension-%{name}
Change a directory colour, then get better visual layout.

%package common
Summary:        Change a directory colour in Caja and Nautilus
Group:          Productivity/File utilities
Requires:       gtk3-tools
Requires:       gvfs
Recommends:     %{name}-common-lang = %{version}

%description common
Change a directory colour, then get better visual layout.

%lang_package -n %{name}-common

%prep
%setup -q -n %{name}-common
%setup -q -D -T -a 1 -n %{name}-common
%setup -q -D -T -a 2 -n %{name}-common
mv -f nautilus %{name}-nautilus

chmod a-x COPYING
sed -i '/name/s/%{name}/%{name}-nautilus/' %{name}-nautilus/setup.py

%build
# Nothing to build.

%install
for dir in . %{name}-caja %{name}-nautilus; do
    pushd $dir
    python2 setup.py install \
      --root=%{buildroot} --prefix=%{_prefix}
    popd
done
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}-common

%post common
%icon_theme_cache_post

%postun common
%icon_theme_cache_postun

%files -n caja-extension-%{name}
%defattr(-,root,root)
%doc COPYING
%{_datadir}/caja-python/
%{python_sitelib}/%{_name}_caja-*

%files -n nautilus-extension-%{name}
%defattr(-,root,root)
%doc COPYING
%{_datadir}/nautilus-python/
%{python_sitelib}/%{_name}_nautilus-*

%files common
%defattr(-,root,root)
%doc COPYING
%{python_sitelib}/%{_name}_common-*
%{_datadir}/icons/hicolor/*/*/

%files common-lang -f %{name}-common.lang
%defattr(-,root,root)

%changelog
