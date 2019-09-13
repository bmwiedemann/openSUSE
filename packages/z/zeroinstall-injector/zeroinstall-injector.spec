#
# spec file for package zeroinstall-injector
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


%define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%define cache_dir /var/cache/0install.net

%if 0%{?suse_version}
%define use_python3 1
%define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%endif

Name:           zeroinstall-injector
Version:        2.3.3
Release:        0
%define source_version 2.3.3
Summary:        Decentralised cross-distribution software installation
License:        LGPL-2.1+
Group:          System/Management

Url:            http://0install.net
Source0:        0install-%{source_version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildArch:      noarch
BuildRequires:  gnupg
BuildRequires:  python-devel
%if 0%{?use_python3}
BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  python3-gobject
%endif

Requires:       binutils
Requires:       gnupg
Requires:       sudo
Requires:       xdg-utils
AutoReqProv:    no

%if 0%{?suse_version}
BuildRequires:  python-xml
Requires:       python-xml
%else
BuildRequires:  PyXML
Requires:       PyXML
%endif

%if 0%{?mandriva_version}
Requires:       pygtk2.0 >= 2.12
BuildRequires:  pygtk2.0
%else
%if 0%{?suse_version}
Requires:       ca-certificates
Requires:       python-gtk >= 2.12
BuildRequires:  python-gtk
BuildRequires:  update-desktop-files
%else
Requires:       pygtk2 >= 2.12
BuildRequires:  pygtk2
%endif
%endif

%description
The Zero Install Injector makes it easy for users to install software without
needing root privileges. It takes the URL of a program and runs it (downloading
it first if necessary). Any dependencies of the program are fetched in the same
way. The user controls which version of the program and its dependencies to
use.

Zero Install is a decentralised installation system (there is no central
repository; all packages are identified by URLs), loosly-coupled (if different
programs require different versions of a library then both versions are
installed in parallel, without conflicts), and has an emphasis on security (all
package descriptions are GPG-signed, and contain cryptographic hashes of the
contents of each version). Each version of each program is stored in its own
sub-directory within the Zero Install cache (nothing is installed to
directories outside of the cache, such as /usr/bin) and no code from the
package is run during install or uninstall. The system can automatically check
for updates when software is run.

%prep
tar xjvf %{SOURCE0}
%setup -q -T -D -n 0install-%{source_version}

%build
python setup.py build
%if 0%{?use_python3}
# (avoids error about missing build/scripts-3.2 directory)
python3 setup.py build
%endif

%check
#(cd tests && python ./testall.py)

%install
# Make Python3 libraries available, but (for now) use Python 2 as the default
# for the commands.
%if 0%{?use_python3}
python3 setup.py install --skip-build --prefix=/usr --root $RPM_BUILD_ROOT
%endif
python setup.py install --skip-build --force --prefix=/usr --root $RPM_BUILD_ROOT
%if 0%{?use_python3}
%fdupes -s %{buildroot}
rm -f $RPM_BUILD_ROOT/%{python3_sitelib}/*.egg-info
%endif
mv "$RPM_BUILD_ROOT/usr/man" "$RPM_BUILD_ROOT%{_datadir}/man"
rm -f $RPM_BUILD_ROOT/%{python_sitelib}/*.egg-info
mkdir -p "$RPM_BUILD_ROOT%{cache_dir}/implementations"
%if 0%{?suse_version}
%suse_update_desktop_file -r 0install Settings DesktopSettings
%endif
%find_lang zero-install
mkdir -p "$RPM_BUILD_ROOT/etc/bash_completion.d/"
ln -s "%{_datadir}/bash-completion/completions/0install" "$RPM_BUILD_ROOT/etc/bash_completion.d/"

%files -f zero-install.lang
%defattr(-,root,root,-)
%doc COPYING README.md
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_bindir}/0*
%{python_sitelib}/zeroinstall
%if 0%{?use_python3}
%{python3_sitelib}/zeroinstall
%endif
%{_mandir}/man1/0*
%{_datadir}/applications/0install.desktop
%{_datadir}/icons/hicolor/scalable/apps/zeroinstall.svg
%{_datadir}/icons/hicolor/128x128/apps/zeroinstall.png
%{_datadir}/icons/hicolor/48x48/apps/zeroinstall.png
%{_datadir}/icons/hicolor/24x24/apps/zeroinstall.png
%{_datadir}/bash-completion/completions/0install
%{_datadir}/fish/completions/0install.fish
%{_datadir}/zsh/site-functions/_0install
/etc/bash_completion.d/0install
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{cache_dir}
%attr(755,zeroinst,zeroinst) %{cache_dir}/implementations

%pre
# Add the "zeroinst" user.
# This is not used by default, but is required if you want to
# set up sharing of downloads later.
/usr/sbin/useradd -c 'Zero Install shared cache' \
        -s /sbin/nologin -r -d '%{cache_dir}' zeroinst 2> /dev/null || :
/usr/sbin/groupadd -r zeroinst 2> /dev/null || :

%changelog
