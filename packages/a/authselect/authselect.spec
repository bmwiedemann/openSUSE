#
# spec file for package authselect
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017-2020 Red Hat, Inc.
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


%global somajor 3
%global libname lib%{name}%{somajor}
%global devname lib%{name}-devel

Name:           authselect
Version:        1.4.3+git.0.87bb4b3
Release:        0
Group:          System/Libraries
Summary:        Configures authentication and identity sources from supported profiles
License:        GPL-3.0-or-later
URL:            https://github.com/authselect/authselect
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-Adapt-authselect-for-the-etc-usr-etc-merge.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libcmocka-devel >= 1.0.0
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  pkgconfig(popt)
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# Optional things that authselect configures
Suggests:       fprintd-pam
Suggests:       oddjob-mkhomedir
Suggests:       samba-winbind
Suggests:       sssd

%description
Authselect is designed to be a replacement for authconfig but it takes
a different approach to configure the system. Instead of letting
the administrator build the PAM stack with a tool (which may potentially
end up with a broken configuration), it would ship several tested stacks
(profiles) that solve a use-case and are well tested and supported.
At the same time, some obsolete features of authconfig are not
supported by authselect.

%package -n %{libname}
Summary:        Utility library used by the authselect tool
Requires:       %{name}-profiles >= %{version}-%{release}
# Package split
Conflicts:      libauthselect1 < %{version}-%{release}
Obsoletes:      libauthselect1 < %{version}-%{release}

%description -n %{libname}
Common library files for authselect. This package is used by the authselect
command line tool and any other potential front-ends.

%package profiles
Summary:        Authentication configuration profiles
BuildArch:      noarch
# Required by scriptlets
Requires(pre):  coreutils
Requires(posttrans):coreutils
Requires(posttrans):findutils
Requires(posttrans):gawk
Requires(posttrans):grep
Requires(posttrans):pam
# >= 1.3.1-23
Requires(posttrans):sed
Requires(posttrans):systemd
# Package split
Conflicts:      libauthselect1 < %{version}-%{release}
Obsoletes:      libauthselect1 < %{version}-%{release}

%description profiles
This package contains the configuration profiles offered by authselect to
allow users to configure authentication on the system.

%package compat
Summary:        Tool to provide minimum backwards compatibility with authconfig
BuildRequires:  python3-devel
Requires:       authselect%{?_isa} = %{version}-%{release}
Recommends:     oddjob-mkhomedir
Suggests:       realmd
Suggests:       samba-winbind
Suggests:       sssd
Provides:       authconfig

%description compat
This package will replace %{_sbindir}/authconfig with a tool that will
translate some of the authconfig calls into authselect calls. It provides
only minimum backward compatibility and users are encouraged to migrate
to authselect completely.

%package lang
Summary:        Language translations for authselect

%description lang
This package contains the language translation files for authselect

%package -n %{devname}
Summary:        Development libraries and headers for authselect
Group:          Development/Libraries/Other
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n %{devname}
System header files and development libraries for authselect. Useful if
you develop a front-end for the authselect library.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --with-pythonbin="%{__python3}" --with-compat
%make_build

%check
%make_build check

%install
%make_install

# Find translations
%find_lang %{name}
%find_lang %{name} %{name}.8.lang --with-man

# We want this file to contain only manual page translations
sed -i '/LC_MESSAGES/d' %{name}.8.lang

# Remove .la and .a files created by libtool
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name "*.a" -exec rm -f {} \;

# Remove /usr/share/doc/authselect, we docify later with rpm...
rm -rf %{buildroot}%{_datadir}/doc/authselect

# Put bash completion in the right location
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/authselect-completion.sh %{buildroot}%{_datadir}/bash-completion/completions/authselect

# Because ldconfig_scriptlets doesn't exist on Leap 15.x... :'(
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%{_libdir}/libauthselect.so.%{somajor}{,.*}

%files profiles
%dir %{_sysconfdir}/authselect
%dir %{_sysconfdir}/authselect/custom
%dir %{_localstatedir}/lib/authselect
%ghost %attr(0755,root,root) %{_localstatedir}/lib/authselect/backups/
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/dconf-db
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/dconf-locks
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/fingerprint-auth
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/nsswitch.conf
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/password-auth
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/postlogin
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/smartcard-auth
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/system-auth
%ghost %attr(0644,root,root) %{_localstatedir}/lib/authselect/user-nsswitch-created
%dir %{_datadir}/authselect
%dir %{_datadir}/authselect/vendor
%dir %{_datadir}/authselect/default
%dir %{_datadir}/authselect/default/minimal/
%dir %{_datadir}/authselect/default/nis/
%dir %{_datadir}/authselect/default/sssd/
%dir %{_datadir}/authselect/default/winbind/
%{_datadir}/authselect/default/minimal/dconf-db
%{_datadir}/authselect/default/minimal/dconf-locks
%{_datadir}/authselect/default/minimal/fingerprint-auth
%{_datadir}/authselect/default/minimal/nsswitch.conf
%{_datadir}/authselect/default/minimal/password-auth
%{_datadir}/authselect/default/minimal/postlogin
%{_datadir}/authselect/default/minimal/README
%{_datadir}/authselect/default/minimal/REQUIREMENTS
%{_datadir}/authselect/default/minimal/smartcard-auth
%{_datadir}/authselect/default/minimal/system-auth
%{_datadir}/authselect/default/nis/dconf-db
%{_datadir}/authselect/default/nis/dconf-locks
%{_datadir}/authselect/default/nis/fingerprint-auth
%{_datadir}/authselect/default/nis/nsswitch.conf
%{_datadir}/authselect/default/nis/password-auth
%{_datadir}/authselect/default/nis/postlogin
%{_datadir}/authselect/default/nis/README
%{_datadir}/authselect/default/nis/REQUIREMENTS
%{_datadir}/authselect/default/nis/smartcard-auth
%{_datadir}/authselect/default/nis/system-auth
%{_datadir}/authselect/default/sssd/dconf-db
%{_datadir}/authselect/default/sssd/dconf-locks
%{_datadir}/authselect/default/sssd/fingerprint-auth
%{_datadir}/authselect/default/sssd/nsswitch.conf
%{_datadir}/authselect/default/sssd/password-auth
%{_datadir}/authselect/default/sssd/postlogin
%{_datadir}/authselect/default/sssd/README
%{_datadir}/authselect/default/sssd/REQUIREMENTS
%{_datadir}/authselect/default/sssd/smartcard-auth
%{_datadir}/authselect/default/sssd/system-auth
%{_datadir}/authselect/default/winbind/dconf-db
%{_datadir}/authselect/default/winbind/dconf-locks
%{_datadir}/authselect/default/winbind/fingerprint-auth
%{_datadir}/authselect/default/winbind/nsswitch.conf
%{_datadir}/authselect/default/winbind/password-auth
%{_datadir}/authselect/default/winbind/postlogin
%{_datadir}/authselect/default/winbind/README
%{_datadir}/authselect/default/winbind/REQUIREMENTS
%{_datadir}/authselect/default/winbind/smartcard-auth
%{_datadir}/authselect/default/winbind/system-auth
%{_mandir}/man5/authselect-profiles.5*

%files compat
%{_sbindir}/authconfig
%{python3_sitelib}/authselect/

%files -n %{devname}
%doc README.md
%{_includedir}/authselect.h
%{_libdir}/libauthselect.so
%{_libdir}/pkgconfig/authselect.pc

%files lang -f %{name}.lang -f %{name}.8.lang

%files
%{_bindir}/authselect
%{_mandir}/man8/authselect.8*
%{_mandir}/man7/authselect-migration.7*
%{_datadir}/bash-completion/completions/authselect

%global validfile %{_localstatedir}/lib/rpm-state/%{name}.config-valid

%pre profiles
# If authselect isn't installed and used, skip
if [ ! -x %{_bindir}/authselect ]; then
    exit 0
fi

if [ -f %{validfile} ]; then
    rm -f %{validfile}
    if [ $1 -gt 1 ]; then
        # Remember if the current configuration is valid
        %{_bindir}/authselect check &> /dev/null
        if [ $? -eq 0 ]; then
            touch %{validfile}
        fi
    fi
fi

exit 0

%posttrans profiles
# If authselect isn't installed and used, skip
if [ ! -x %{_bindir}/authselect ]; then
    exit 0
fi

# Copy nsswitch.conf to user-nsswitch.conf if it was not yet created
if [ ! -f %{_localstatedir}/lib/authselect/user-nsswitch-created ]; then
    cp -n %{_sysconfdir}/nsswitch.conf %{_sysconfdir}/authselect/user-nsswitch.conf &> /dev/null
    touch %{_localstatedir}/lib/authselect/user-nsswitch-created &> /dev/null

    # If we are upgrading from older version, we want to remove these comments.
    sed -i '/^# Generated by authselect on .*$/{$!{
      N;N # Read also next two lines
      /# Generated by authselect on .*\n# Do not modify this file manually.\n/d
    }}' %{_sysconfdir}/authselect/user-nsswitch.conf &> /dev/null
fi

# If the configuration is valid and we are upgrading from older version
# we need to create these files since they were added in 1.0.
if [ -f %{validfile} ]; then
    FILES="nsswitch.conf system-auth password-auth fingerprint-auth \
           smartcard-auth postlogin dconf-db dconf-locks"

    for FILE in $FILES ; do
        cp -n %{_sysconfdir}/authselect/$FILE \
               %{_localstatedir}/lib/authselect/$FILE &> /dev/null
    done

    rm -f %{validfile}
fi

# Apply any changes to profiles (validates configuration first internally)
%{_bindir}/authselect apply-changes &> /dev/null

# Enable with-sudo feature if sssd-sudo responder is enabled. RHBZ#1582111
CURRENT=`%{_bindir}/authselect current --raw 2> /dev/null`
if [ $? -eq 0 ]; then
    PROFILE=`echo $CURRENT | gawk '{print $1;}'`

    if [ "$PROFILE" = "sssd" ] ; then
        if grep -E "services[[:blank:]]*=[[:blank:]]*.*sudo" %{_sysconfdir}/sssd/sssd.conf &> /dev/null ; then
            %{_bindir}/authselect enable-feature with-sudo &> /dev/null
        elif systemctl is-active sssd-sudo.service sssd-sudo.socket --quiet || systemctl is-enabled sssd-sudo.socket --quiet ; then
            %{_bindir}/authselect enable-feature with-sudo &> /dev/null
        fi
    fi
fi

exit 0

%changelog
