#
# spec file for package libreport
#
# Copyright (c) 2019-2024 Red Hat, Inc.
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


%define glib_ver 2.43.4

%if 0%{?suse_version}
  %bcond_without bugzilla
%else
  %bcond_with bugzilla
%endif
Name:           libreport
Version:        2.17.15
Release:        1%{?dist}
Summary:        Generic library for reporting various problems
License:        GPL-2.0-or-later
URL:            https://abrt.readthedocs.org/
Source:         https://github.com/abrt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         opensuse_workflow.patch
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  asciidoc
BuildRequires:  augeas
BuildRequires:  pkgconfig(augeas)
BuildRequires:  augeas-lenses
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_ver}
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  libtool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  make
BuildRequires:  pkgconfig(libnewt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(satyr) >= 0.38
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  texinfo
BuildRequires:  xmlto
Requires:       glib2-tools%{?_isa} >= %{glib_ver}
Requires:       libreport-filesystem = %{version}-%{release}
Requires:       satyr%{?_isa} >= 0.38
Obsoletes:      %{name}-compat < 2.13.2
Obsoletes:      %{name}-plugin-rhtsupport < 2.13.2
Obsoletes:      %{name}-rhel < 2.13.2
%if 0%{?fedora} >= 24 || 0%{?rhel} > 7
# A test case uses zh_CN locale to verify XML event translations
BuildRequires:  glibc-all-langpacks
%endif
%if %{with bugzilla}
BuildRequires:  pkgconfig(xmlrpc_client)
%endif
# Required for the temporary modularity hack, see below
%if 0%{?_module_build}
BuildRequires:  sed
%endif

%description
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc.

%package -n libreport_2
Summary:        Generic library for reporting various problems

%description -n libreport_2
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc.

%package filesystem
Summary:        Filesystem layout for libreport
BuildArch:      noarch

%description filesystem
Filesystem layout for libreport

%package devel
Summary:        Development libraries and headers for libreport
Requires:       libreport_2 = %{version}-%{release}

%description devel
Development libraries and headers for libreport

%package web_2
Summary:        Library providing network API for libreport
Requires:       libreport_2 = %{version}-%{release}

%description web_2
Library providing network API for libreport

%package web_2-devel
Summary:        Development headers for libreport-web
Requires:       libreport-web_2 = %{version}-%{release}

%description web_2-devel
Development headers for libreport-web

%package -n python3-libreport
%{?python_provide:%python_provide python3-libreport}
Requires:       libreport_2 = %{version}-%{release}
Summary:        Python 3 bindings for report-libs
Requires:       python3-dnf
Requires:       python3-requests
#Requires:       python3-urllib3

%description -n python3-libreport
Python 3 bindings for report-libs.

%package cli
Summary:        %{name} command line interface
Requires:       libreport_2 = %{version}-%{release}

%description cli
This package contains simple command line tool for working
with problem dump reports

%package newt
Summary:        %{name}'s newt interface
Requires:       libreport_2 = %{version}-%{release}
Provides:       report-newt = 0:0.23-1
Obsoletes:      report-newt < 0:0.23-1

%description newt
This package contains a simple newt application for reporting
bugs

%package gtk_1
Summary:        GTK front-end for libreport
Requires:       libreport-plugin-reportuploader = %{version}
Requires:       libreport_2 = %{version}
Provides:       report-gtk = 0:0.23-1
Obsoletes:      report-gtk < 0:0.23-1

%description gtk_1
Applications for reporting bugs using libreport backend

%package gtk_1-devel
Summary:        Development libraries and headers for libreport
Requires:       libreport-gtk_1 = %{version}-%{release}

%description gtk_1-devel
Development libraries and headers for libreport-gtk

%package plugin-kerneloops
Summary:        %{name}'s kerneloops reporter plugin
Requires:       curl
Requires:       libreport-web_2 = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to specified
server, usually to kerneloops.org.

%package plugin-logger
Summary:        %{name}'s logger reporter plugin
Requires:       libreport_2 = %{version}-%{release}

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%package plugin-systemd-journal
Summary:        %{name}'s systemd journal reporter plugin
Requires:       libreport_2 = %{version}-%{release}

%description plugin-systemd-journal
The simple reporter plugin which writes a report to the systemd journal.

%package plugin-mailx
Summary:        %{name}'s mailx reporter plugin
Requires:       %{_bindir}/mailx
Requires:       libreport_2 = %{version}-%{release}

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a specified
email address.

%if %{with bugzilla}
%package plugin-bugzilla
Summary:        %{name}'s bugzilla plugin
Requires:       libreport-web_2 = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}
Requires:       python3-libreport = %{version}-%{release}
%if 0%{?fedora} >= 38
Requires:       python3-satyr
Suggests:       python3-pytest
Suggests:       python3-vcrpy
%endif

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.
%endif

%package plugin-mantisbt
Summary:        %{name}'s mantisbt plugin
Requires:       libreport-web_2 = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}

%description plugin-mantisbt
Plugin to report bugs into the mantisbt.

%package centos
Summary:        %{name}'s CentOS Bug Tracker workflow
Requires:       libreport-plugin-mantisbt = %{version}-%{release}
Requires:       libreport-web_2 = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}
BuildArch:      noarch

%description centos
Workflows to report issues into the CentOS Bug Tracker.

%package plugin-ureport
Summary:        %{name}'s micro report plugin
BuildRequires:  pkgconfig(json-c)
Requires:       libreport-web_2 = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}

%description plugin-ureport
Uploads micro-report to abrt server

%package plugin-reportuploader
Summary:        %{name}'s reportuploader plugin
Requires:       libreport-web_2 = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with ticketing system.

%if 0%{?fedora} || 0%{?eln}
%package fedora
Summary:        Default configuration for reporting bugs via Fedora infrastructure
Requires:       libreport_2 = %{version}-%{release}

%description fedora
Default configuration for reporting bugs via Fedora infrastructure
used to easily configure the reporting process for Fedora systems. Just
install this package and you're done.
%endif

%if 0%{?rhel} && ! 0%{?eln}
%package rhel-bugzilla
Summary:        Default configuration for reporting bugs to Red Hat Bugzilla
Requires:       libreport-plugin-bugzilla = %{version}-%{release}
Requires:       libreport-plugin-ureport = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}

%description rhel-bugzilla
Default configuration for reporting bugs to Red Hat Bugzilla used to easily
configure the reporting process for Red Hat systems. Just install this package
and you're done.

%package rhel-anaconda-bugzilla
Summary:        Default configuration for reporting anaconda bugs to Red Hat Bugzilla
Requires:       libreport-plugin-bugzilla = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}

%description rhel-anaconda-bugzilla
Default configuration for reporting Anaconda problems to Red Hat Bugzilla used
to easily configure the reporting process for Red Hat systems. Just install this
package and you're done.
%endif

%if 0%{?suse_version}
%package opensuse-bugzilla
Summary:        Default configuration for reporting bugs to openSUSE Bugzilla
Requires:       libreport-plugin-bugzilla = %{version}-%{release}
Requires:       libreport-plugin-ureport = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}
BuildArch:      noarch

%description opensuse-bugzilla
Default configuration for reporting bugs to openSUSE Bugzilla used to easily
configure the reporting process for Red Hat systems. Just install this package
and you're done.
%endif

%if %{with bugzilla}
%package anaconda
Summary:        Default configuration for reporting anaconda bugs
Requires:       libreport-plugin-reportuploader = %{version}-%{release}
Requires:       libreport_2 = %{version}-%{release}
BuildArch:      noarch
%if ! 0%{?rhel} || 0%{?eln}
Requires:       libreport-plugin-bugzilla = %{version}-%{release}
%endif

%description anaconda
Default configuration for reporting Anaconda problems or uploading the gathered
data over ftp/scp...
%endif

%prep
%autosetup -n libreport-%{version} -p1

%build
./autogen.sh

%configure \
%if %{without bugzilla}
        --without-bugzilla \
%endif
        --enable-doxygen-docs \
        --disable-silent-rules

%make_build

%install
%make_install \
%if %{with python3}
             PYTHON=python3 \
%endif
             mandir=%{_mandir}

%find_lang %{name}

# Remove byte-compiled python files generated by automake.
# automake uses system's python for all *.py files, even
# for those which needs to be byte-compiled with different
# version (python2/python3).
# rpm can do this work and use the appropriate python version.
find %{buildroot} -name "*.py[co]" -delete

# remove all .la and .a files
find %{buildroot} "(" -name '*.la' -or -name '*.a' ")" -delete
mkdir -p %{buildroot}/%{_initddir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/events.d/
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/events/
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/workflows.d/
mkdir -p %{buildroot}/%{_datadir}/%{name}/events/
mkdir -p %{buildroot}/%{_datadir}/%{name}/workflows/

# After everything is installed, remove info dir
rm -f %{buildroot}/%{_infodir}/dir

# Remove unwanted Fedora specific workflow configuration files
%if ! 0%{?fedora} && ! 0%{?eln}
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraCCpp.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraKerneloops.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraPython.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraPython3.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraVmcore.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraXorg.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraLibreport.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraJava.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_FedoraJavaScript.xml
rm -f %{buildroot}/%{_sysconfdir}/libreport/workflows.d/report_fedora.conf
rm -f %{buildroot}%{_mandir}/man5/report_fedora.conf.5
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_AnacondaFedora.xml
%endif

# Remove unwanted RHEL specific workflow configuration files
%if ! 0%{?rhel} || 0%{?eln}
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_uReport.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_AnacondaRHELBugzilla.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaCCpp.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaKerneloops.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaPython.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaVmcore.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaXorg.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaLibreport.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaJava.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELBugzillaJavaScript.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataCCpp.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataKerneloops.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataPython.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDatavmcore.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataxorg.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataLibreport.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataJava.xml
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_RHELAddDataJavaScript.xml
rm -f %{buildroot}/%{_sysconfdir}/libreport/workflows.d/report_uReport.conf
rm -f %{buildroot}/%{_sysconfdir}/libreport/workflows.d/report_rhel_bugzilla.conf
rm -f %{buildroot}%{_mandir}/man5/report_uReport.conf.5
rm -f %{buildroot}%{_mandir}/man5/report_rhel_bugzilla.conf.5
%endif

# Remove unwanted SUSE specific workflow configuration files
%if ! 0%{?suse_version}
rm -f %{buildroot}/%{_datadir}/libreport/workflows/workflow_openSUSEBugzillaPython.xml
rm -f %{buildroot}%{_mandir}/man5/report_rhel_bugzilla.conf.5
%endif


%if 0%{?fedora} >= 38
    mv %{buildroot}/%{_bindir}/reporter-bugzilla-python %{buildroot}/%{_bindir}/reporter-bugzilla
%endif

%check
# tmp commented out since it is broken
#make check|| {
#    # find and print the logs of failed test
#    # do not cat tests/testsuite.log because it contains a lot of bloat
#    find tests/testsuite.dir -name "testsuite.log" -print -exec cat '{}' \;
#    exit 1
#}

%{ldconfig_scriptlets}
%{ldconfig_scriptlets web_2}
%{ldconfig_scriptlets gtk_1}
%{ldconfig_scriptlets -n libreport_2}

%if 0%{?rhel} && 0%{?rhel} <= 7
%post gtk
%{?ldconfig}
# update icon cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun gtk
%{?ldconfig}
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans gtk
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%endif

# separate shlibs - openSUSE guidelines
%if 0%{?suse_version}
%files -f %{name}.lang 
%doc README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}/libreport.conf
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%config(noreplace) %{_sysconfdir}/%{name}/forbidden_words.conf
%config(noreplace) %{_sysconfdir}/%{name}/ignored_words.conf
%config(noreplace) %{_sysconfdir}/%{name}/ignored_elements.conf
%{_datadir}/%{name}/conf.d/libreport.conf
%{_mandir}/man5/libreport.conf.5%{?ext_man}
%{_mandir}/man5/report_event.conf.5%{?ext_man}
%{_mandir}/man5/forbidden_words.conf.5%{?ext_man}
%{_mandir}/man5/ignored_words.conf.5%{?ext_man}
%{_mandir}/man5/ignored_elements.conf.5%{?ext_man}
# filesystem package owns /usr/share/augeas/lenses directory
%{_datadir}/augeas/lenses/libreport.aug

%else

%files -f %{name}.lang -n libreport_2
%doc README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}/libreport.conf
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%config(noreplace) %{_sysconfdir}/%{name}/forbidden_words.conf
%config(noreplace) %{_sysconfdir}/%{name}/ignored_words.conf
%config(noreplace) %{_sysconfdir}/%{name}/ignored_elements.conf
%{_datadir}/%{name}/conf.d/libreport.conf
%{_libdir}/libreport.so.*
%{_libdir}/libreport.so.*.*.*
%{_mandir}/man5/libreport.conf.5%{?ext_man}
%{_mandir}/man5/report_event.conf.5%{?ext_man}
%{_mandir}/man5/forbidden_words.conf.5%{?ext_man}
%{_mandir}/man5/ignored_words.conf.5%{?ext_man}
%{_mandir}/man5/ignored_elements.conf.5%{?ext_man}
# filesystem package owns /usr/share/augeas/lenses directory
%{_datadir}/augeas/lenses/libreport.aug
%endif


# separate shlibs - openSUSE guidelines
%if 0%{?suse_version}
%files -n libreport_2
%license COPYING
%{_libdir}/libreport.so.*
%endif

%files filesystem
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/events.d/
%dir %{_sysconfdir}/%{name}/events/
%dir %{_sysconfdir}/%{name}/workflows.d/
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/conf.d/
%dir %{_datadir}/%{name}/conf.d/plugins/
%dir %{_datadir}/%{name}/events/
%dir %{_datadir}/%{name}/workflows/
%dir %{_sysconfdir}/%{name}/plugins/

%files devel
# Public api headers:
%doc apidoc/html/*.{html,png,css,js}
%{_includedir}/libreport/libreport_types.h
%{_includedir}/libreport/client.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/problem_report.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/report_result.h
%{_includedir}/libreport/run_event.h
%{_includedir}/libreport/file_obj.h
%{_includedir}/libreport/config_item_info.h
%{_includedir}/libreport/workflow.h
%{_includedir}/libreport/problem_details_widget.h
%{_includedir}/libreport/problem_details_dialog.h
%{_includedir}/libreport/problem_utils.h
%{_includedir}/libreport/ureport.h
%{_includedir}/libreport/reporters.h
%{_includedir}/libreport/global_configuration.h
# Private api headers:
%{_includedir}/libreport/internal_libreport.h
%{_includedir}/libreport/xml_parser.h
%{_includedir}/libreport/helpers
%{_libdir}/libreport.so
%{_libdir}/pkgconfig/libreport.pc
%dir %{_includedir}/libreport

# separate shlibs - openSUSE guidelines
%if 0%{?suse_version}
%files web_2
%{_libdir}/libreport-web.so.*

%files web_2-devel
%{_includedir}/libreport/libreport_curl.h
%{_libdir}/pkgconfig/libreport-web.pc
%{_libdir}/libreport-web.so
%else
%files web_2
%{_libdir}/libreport-web.so.*
%{_libdir}/libreport-web.so.*.*.*

%files web_2-devel
%{_includedir}/libreport/libreport_curl.h
%{_libdir}/pkgconfig/libreport-web.pc
%{_libdir}/libreport-web.so
%endif

%files -n python3-libreport
%{python3_sitearch}/report/
%{python3_sitearch}/reportclient/

%files cli
%{_bindir}/report-cli
%{_mandir}/man1/report-cli.1%{?ext_man}

%files newt
%{_bindir}/report-newt
%{_mandir}/man1/report-newt.1%{?ext_man}


# separate shlibs - openSUSE guidelines
%if 0%{?suse_version}
%files gtk_1
%{_libdir}/libreport-gtk.so.*

%files gtk_1-devel
%{_bindir}/report-gtk
%{_includedir}/libreport/internal_libreport_gtk.h
%{_libdir}/pkgconfig/libreport-gtk.pc
%{_mandir}/man1/report-gtk.1%{?ext_man}
%{_libdir}/libreport-gtk.so
%else
%files gtk_1
%{_bindir}/report-gtk
%{_libdir}/libreport-gtk.so.*
%{_libdir}/libreport-gtk.so.*.*.*
%{_mandir}/man1/report-gtk.1%{?ext_man}

%files gtk_1-devel
%{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_libdir}/pkgconfig/libreport-gtk.pc
%endif

%files plugin-kerneloops
%{_datadir}/%{name}/events/report_Kerneloops.xml
%{_mandir}/man*/reporter-kerneloops.*
%{_bindir}/reporter-kerneloops

%files plugin-logger
%config(noreplace) %{_sysconfdir}/libreport/events/report_Logger.conf
%{_mandir}/man5/report_Logger.conf.5%{?ext_man}
%{_datadir}/%{name}/events/report_Logger.xml
%{_datadir}/%{name}/workflows/workflow_Logger.xml
%{_datadir}/%{name}/workflows/workflow_LoggerCCpp.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_logger.conf
%{_mandir}/man5/print_event.conf.5%{?ext_man}
%{_mandir}/man5/report_logger.conf.5%{?ext_man}
%{_bindir}/reporter-print
%{_mandir}/man*/reporter-print.*

%files plugin-systemd-journal
%{_bindir}/reporter-systemd-journal
%{_mandir}/man*/reporter-systemd-journal.*

%files plugin-mailx
%config(noreplace) %{_sysconfdir}/libreport/plugins/mailx.conf
%{_datadir}/%{name}/conf.d/plugins/mailx.conf
%{_datadir}/%{name}/events/report_Mailx.xml
%{_datadir}/%{name}/workflows/workflow_Mailx.xml
%{_datadir}/%{name}/workflows/workflow_MailxCCpp.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_mailx.conf
%{_mandir}/man5/mailx.conf.5%{?ext_man}
%{_mandir}/man5/mailx_event.conf.5%{?ext_man}
%{_mandir}/man5/report_mailx.conf.5%{?ext_man}
%{_mandir}/man*/reporter-mailx.*
%{_bindir}/reporter-mailx

%files plugin-ureport
%config(noreplace) %{_sysconfdir}/libreport/plugins/ureport.conf
%{_datadir}/%{name}/conf.d/plugins/ureport.conf
%{_bindir}/reporter-ureport
%{_mandir}/man1/reporter-ureport.1%{?ext_man}
%{_mandir}/man5/ureport.conf.5%{?ext_man}
%{_datadir}/%{name}/events/report_uReport.xml
%if 0%{?rhel} && ! 0%{?eln}
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_uReport.conf
%{_datadir}/%{name}/workflows/workflow_uReport.xml
%{_mandir}/man5/report_uReport.conf.5%{?ext_man}
%endif

%if %{with bugzilla}
%files plugin-bugzilla
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%{_datadir}/%{name}/conf.d/plugins/bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_analyzer_libreport.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup_analyzer_libreport.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_kernel.conf
%{_datadir}/%{name}/events/report_Bugzilla.xml
%{_datadir}/%{name}/events/watch_Bugzilla.xml
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
# FIXME: remove with the old gui
%{_mandir}/man1/reporter-bugzilla.1%{?ext_man}
%{_mandir}/man5/report_Bugzilla.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_event.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_format.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_formatdup.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_format_analyzer_libreport.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_formatdup_analyzer_libreport.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_format_kernel.conf.5%{?ext_man}
%{_bindir}/reporter-bugzilla
%if 0%{?fedora} < 38
%{_bindir}/reporter-bugzilla-python
%endif

%endif

%files plugin-mantisbt
%config(noreplace) %{_sysconfdir}/libreport/plugins/mantisbt.conf
%{_datadir}/%{name}/conf.d/plugins/mantisbt.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/mantisbt_format.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/mantisbt_formatdup.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/mantisbt_format_analyzer_libreport.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/mantisbt_formatdup_analyzer_libreport.conf
%{_bindir}/reporter-mantisbt
%{_mandir}/man1/reporter-mantisbt.1%{?ext_man}
%{_mandir}/man5/mantisbt.conf.5%{?ext_man}
%{_mandir}/man5/mantisbt_format.conf.5%{?ext_man}
%{_mandir}/man5/mantisbt_formatdup.conf.5%{?ext_man}
%{_mandir}/man5/mantisbt_format_analyzer_libreport.conf.5%{?ext_man}
%{_mandir}/man5/mantisbt_formatdup_analyzer_libreport.conf.5%{?ext_man}

%files centos
%{_datadir}/%{name}/workflows/workflow_CentOSCCpp.xml
%{_datadir}/%{name}/workflows/workflow_CentOSKerneloops.xml
%{_datadir}/%{name}/workflows/workflow_CentOSPython.xml
%{_datadir}/%{name}/workflows/workflow_CentOSPython3.xml
%{_datadir}/%{name}/workflows/workflow_CentOSVmcore.xml
%{_datadir}/%{name}/workflows/workflow_CentOSXorg.xml
%{_datadir}/%{name}/workflows/workflow_CentOSLibreport.xml
%{_datadir}/%{name}/workflows/workflow_CentOSJava.xml
%{_datadir}/%{name}/workflows/workflow_CentOSJavaScript.xml
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_centos.conf
%{_mandir}/man5/report_centos.conf.5%{?ext_man}
%{_datadir}/%{name}/events/report_CentOSBugTracker.xml
%config(noreplace) %{_sysconfdir}/libreport/events/report_CentOSBugTracker.conf
%{_mandir}/man5/report_CentOSBugTracker.conf.5%{?ext_man}
# report_CentOSBugTracker events are shipped by libreport package
%config(noreplace) %{_sysconfdir}/libreport/events.d/centos_report_event.conf
%{_mandir}/man5/centos_report_event.conf.5%{?ext_man}

%files plugin-reportuploader
%{_mandir}/man*/reporter-upload.*
%{_mandir}/man5/uploader_event.conf.5%{?ext_man}
%{_bindir}/reporter-upload
%{_datadir}/%{name}/events/report_Uploader.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf
%{_datadir}/%{name}/workflows/workflow_Upload.xml
%{_datadir}/%{name}/workflows/workflow_UploadCCpp.xml
%config(noreplace) %{_sysconfdir}/libreport/plugins/upload.conf
%{_datadir}/%{name}/conf.d/plugins/upload.conf
%{_mandir}/man5/upload.conf.5%{?ext_man}
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_uploader.conf
%{_mandir}/man5/report_uploader.conf.5%{?ext_man}
%config(noreplace) %{_sysconfdir}/libreport/events/report_Uploader.conf
%{_mandir}/man5/report_Uploader.conf.5%{?ext_man}

%if 0%{?fedora} || 0%{?eln}
%files fedora
%{_datadir}/%{name}/workflows/workflow_FedoraCCpp.xml
%{_datadir}/%{name}/workflows/workflow_FedoraKerneloops.xml
%{_datadir}/%{name}/workflows/workflow_FedoraPython.xml
%{_datadir}/%{name}/workflows/workflow_FedoraPython3.xml
%{_datadir}/%{name}/workflows/workflow_FedoraVmcore.xml
%{_datadir}/%{name}/workflows/workflow_FedoraXorg.xml
%{_datadir}/%{name}/workflows/workflow_FedoraLibreport.xml
%{_datadir}/%{name}/workflows/workflow_FedoraJava.xml
%{_datadir}/%{name}/workflows/workflow_FedoraJavaScript.xml
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_fedora.conf
%{_mandir}/man5/report_fedora.conf.5%{?ext_man}
%endif

%if %{with bugzilla}
%if 0%{?rhel} && ! 0%{?eln}
%files rhel-bugzilla
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaCCpp.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaKerneloops.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaPython.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaVmcore.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaXorg.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaLibreport.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaJava.xml
%{_datadir}/%{name}/workflows/workflow_RHELBugzillaJavaScript.xml
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_rhel_bugzilla.conf
%{_mandir}/man5/report_rhel_bugzilla.conf.5%{?ext_man}

%files rhel-anaconda-bugzilla
%{_datadir}/%{name}/workflows/workflow_AnacondaRHELBugzilla.xml
%endif

%if 0%{?suse_version}
%files opensuse-bugzilla
%{_datadir}/%{name}/workflows/workflow_openSUSEBugzillaPython.xml
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_opensuse_bugzilla.conf
%{_mandir}/man5/report_opensuse_bugzilla.conf.5%{?ext_man}
%endif

%files anaconda
%if 0%{?fedora} || 0%{?eln}
%{_datadir}/%{name}/workflows/workflow_AnacondaFedora.xml
%endif
%{_datadir}/%{name}/workflows/workflow_AnacondaUpload.xml
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/anaconda_event.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_anaconda_event.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_anaconda.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup_anaconda.conf
%{_mandir}/man5/anaconda_event.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_anaconda_event.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_format_anaconda.conf.5%{?ext_man}
%{_mandir}/man5/bugzilla_formatdup_anaconda.conf.5%{?ext_man}
%endif

%changelog
