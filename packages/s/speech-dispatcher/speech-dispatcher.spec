#
# spec file for package speech-dispatcher
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


%global flavor @BUILD_FLAVOR@%{nil}
%if 0%{?suse_version} >= 1500
%define espeak     espeak-ng
%define espeakdev  espeak-ng-devel
%define espeak_lib libespeak-ng1
%else
%define espeak     espeak
%define espeakdev  espeak-devel
%define espeak_lib espeak
%endif
%if 0%{?suse_version} > 1500
%define _python %{primary_python}
%if "%{flavor}" == "python311"
ExclusiveArch:  do-not-build
%endif
%else
%if "%{flavor}" == "python311"
%{?sle15_python_module_pythons}
%define _python python311
%define python_sitearch %{?python_sitearch:%python311_sitearch}
%else
%define _python python3
%define python_sitearch %{?python_sitearch:%python3_sitearch}
%endif
%endif

%if "%{flavor}" == ""
Name:           speech-dispatcher
%else
Name:           speech-dispatcher-%{_python}
%endif
Version:        0.12.0~rc3
Release:        0
# FIXME missing backends: festival lite, ibmeci (ibm tts), dumbtts/ivona, nas
# The API and bindings are LGPL-2.1-or-later, other parts are
# either GPL-2.0-or-later or LGPL-2.1-or-later
Summary:        Device independent layer for speech synthesis
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Daemons
URL:            https://devel.freebsoft.org/speechd
Source0:        https://github.com/brailcom/speechd/releases/download/0.12.0-rc3/speech-dispatcher-0.12.0-rc3.tar.gz
Patch0:         harden_speech-dispatcherd.service.patch
# PATCH-FIX-UPSTREAM speech-dispatcher-missing-return-vals.patch
Patch1:         speech-dispatcher-missing-return-vals.patch
# PATCH-FIX-OPENSUSE speech-dispatcher-pulseaudio-samples.patch
Patch2:         speech-dispatcher-pulseaudio-samples.patch
# Logrotate file taken from Debian
Source2:        speech-dispatcher.logrotate
Source99:       baselibs.conf
BuildRequires:  %{_python}-setuptools
BuildRequires:  %{espeakdev}
BuildRequires:  alsa-devel
BuildRequires:  dotconf-devel
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  libao-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
Suggests:       festival
Suggests:       logrotate
Provides:       speechd = %{version}
Obsoletes:      speechd < %{version}
# In 12.1, with GNOME 3, gnome-speech is completely deprecated and
# speech-dispatcher replaces it. We don't have a Provides since this is
# really just about obsoleting at technology, not providing it.
Obsoletes:      gnome-speech <= 0.4.25
%{?systemd_ordering}

%description
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%package configure
Summary:        Configuration tool for Speech Dispatcher
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Daemons
Requires:       %{_python}-pyxdg
Requires:       %{_python}-speechd
Requires:       %{name} = %{version}
Enhances:       %{name}

%description configure
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

This package contains spd-conf, a configuration tool for Speech
Dispatcher.

%package module-espeak
Summary:        ESpeak module for Speech Dispatcher
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:%{espeak_lib})

%description module-espeak
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

This package contains the espeak module.

%package -n libspeechd2
Summary:        Device independent layer for speech synthesis - Client library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Recommends:     %{name}

%description -n libspeechd2
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%package -n libspeechd-devel
Summary:        Device independent layer for speech synthesis - Development files
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
Requires:       libspeechd2 = %{version}
Provides:       %{name}-devel = %{version}
Provides:       speechd-devel = %{version}
Obsoletes:      speechd-devel < %{version}

%description -n libspeechd-devel
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%package -n %{_python}-speechd
Summary:        Device independent layer for speech synthesis - Python Bindings
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
Requires:       speech-dispatcher >= %{version}
%if 0%{?suse_version} > 1500
Provides:       python3-speechd = %{version}
Obsoletes:      python3-speechd < %{version}
%endif

%description -n %{_python}-speechd
The goal of Speech Dispatcher project is to provide a high-level device
independent layer for speech synthesis through a simple, stable and
well documented interface.

What is a very high level GUI library to graphics, Speech Dispatcher is
to speech synthesis. The application neither needs to talk to the
devices directly nor to handle concurrent access, sound output and other
tricky aspects of the speech subsystem.

%prep
%autosetup -p1 -n speech-dispatcher-0.12.0-rc3
# dummy module must almost never be disabled
sed -i "s/#AddModule \"dummy\"/AddModule \"dummy\"/" -i config/speechd.conf
# you must enable at least one module (except dummy), otherwise it will load
# all available modules and may cause huge cpu usage!
sed -i "s/#AddModule \"%{espeak}\"/AddModule \"%{espeak}\"/" -i config/speechd.conf

sed -i '1{\,^#!%{_bindir}/env python,d}' src/api/python/speechd/_test.py

%build
%global optflags %{optflags} -fcommon
%if "%{flavor}" == "python311"
export PYTHON=/usr/bin/python3.11
%endif
%configure --disable-static \
        --with-libao \
        --with-alsa \
        --with-pulse \
        --without-baratinoo \
        --without-flite \
        --without-kali \
        --with-ibmtts=no \
        --with-voxin=no
%if "%{flavor}" == "python311"
cd src/api/python/speechd
%endif
%make_build

%install
%if "%{flavor}" == "python311"
cd src/api/python/speechd
%endif
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if "%{flavor}" == ""
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcspeech-dispatcherd
# Create log dir. 0700 since the logs can contain user information.
install -d -m 0700 %{buildroot}%{_localstatedir}/log/speech-dispatcher/
# Install logrotate script
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
install -D -m 0644 %{SOURCE2} %{buildroot}%{_distconfdir}/logrotate.d/speech-dispatcher
%else
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/speech-dispatcher
%endif
# Remove config files for modules we don't support
rm %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/flite.conf
rm -f %{buildroot}%{_sysconfdir}/speech-dispatcher/modules/ibmtts.conf
# Remove config files that we don't need a second time
# but then user can not create its own configuration, because here is default, while in /etc is system-wide
# %%{__rm} -r %%{buildroot}%%{_datadir}/speech-dispatcher/conf/
# Remove %%{_infodir}/dir file if it exists
test -d %{buildroot}%{_infodir}/dir && rm %{buildroot}%{_infodir}/dir
%find_lang %{name}
# rpmlint
%{python_expand # Fix shebang path
sed -i "1s|#\!.*python.*|#\!/usr/bin/$python|" %{buildroot}%{_bindir}/spd-conf
}
%endif

# Deduplicate python bytecode
%fdupes %{buildroot}%{python_sitearch}/speechd*
# Deduplicate locale files
%fdupes %{buildroot}%{_datadir}/speech-dispatcher/locale

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/spd-say.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ssip.info.gz
%service_add_post speech-dispatcherd.service

%pre
%service_add_pre speech-dispatcherd.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/speech-dispatcher ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%preun
%service_del_preun speech-dispatcherd.service

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/spd-say.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ssip.info.gz
%service_del_postun speech-dispatcherd.service

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/speech-dispatcher ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post -n libspeechd2 -p /sbin/ldconfig

%postun -n libspeechd2 -p /sbin/ldconfig

%if "%{flavor}" == ""
%files -f %{name}.lang
%doc AUTHORS ANNOUNCE NEWS README.md
%license COPYING.LGPL COPYING.GPL-2 COPYING.GPL-3
%dir %{_sysconfdir}/speech-dispatcher/
%dir %{_sysconfdir}/speech-dispatcher/clients
%dir %{_sysconfdir}/speech-dispatcher/modules
%config(noreplace) %{_sysconfdir}/speech-dispatcher/speechd.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/clients/*.conf
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/*.conf
%exclude %{_sysconfdir}/speech-dispatcher/modules/espeak.conf
%{_bindir}/*
%exclude %{_bindir}/spd-conf
%{_datadir}/sounds/speech-dispatcher/
%dir %{_libdir}/speech-dispatcher
%{_libdir}/speech-dispatcher/spd_*.so
# When adding a module, also stop removing its config file in %%install
%dir %{_libexecdir}/speech-dispatcher-modules
%{_libexecdir}/speech-dispatcher-modules/sd_cicero
%{_libexecdir}/speech-dispatcher-modules/sd_dummy
%{_libexecdir}/speech-dispatcher-modules/sd_festival
%{_libexecdir}/speech-dispatcher-modules/sd_generic
%{_libexecdir}/speech-dispatcher-modules/sd_openjtalk
%{_infodir}/%{name}*.info.gz
%{_infodir}/spd-say.info.gz
%{_infodir}/ssip.info.gz
# logs
%dir %attr(0700, root, root) %{_localstatedir}/log/speech-dispatcher/
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/speech-dispatcher
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/speech-dispatcher
%endif
# systemd service file
%{_unitdir}/speech-dispatcherd.service
%{_userunitdir}/speech-dispatcher.service
%{_userunitdir}/speech-dispatcher.socket
%{_sbindir}/rcspeech-dispatcherd
%{_datadir}/speech-dispatcher/

%files configure
%{_bindir}/spd-conf
%{python_sitearch}/speechd_config/

%files module-espeak
%config(noreplace) %{_sysconfdir}/speech-dispatcher/modules/espeak.conf
%{_libexecdir}/speech-dispatcher-modules/sd_%{espeak}
%{_libexecdir}/speech-dispatcher-modules/sd_%{espeak}-mbrola

%files -n libspeechd2
%{_libdir}/libspeechd.so.*

%files -n libspeechd-devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%endif

%files -n %{_python}-speechd
%{python_sitearch}/speechd/
%pycache_only %{python_sitearch}/speechd/__pycache__

%changelog
