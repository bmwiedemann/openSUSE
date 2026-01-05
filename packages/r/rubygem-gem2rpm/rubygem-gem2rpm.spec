#
# spec file for package rubygem-gem2rpm
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_without  gem2rpm_bootstrap
%bcond_with     ruby21
%bcond_with     ruby25
%bcond_with     ruby32
%bcond_with     ruby33
%bcond_with     ruby34
%bcond_with     ruby35
%bcond_with     ruby40

Name:           rubygem-gem2rpm
Version:        0.10.1
Release:        0
%define mod_name gem2rpm
%define mod_full_name %{mod_name}-%{version}
%define mod_branch -%{version}
%define mod_weight 1001
%if %{with ruby21}
BuildRequires:  ruby2.1
%endif
%if %{with ruby25}
BuildRequires:  ruby2.5
%endif
%if %{with ruby32}
BuildRequires:  ruby3.2
%endif
%if %{with ruby33}
BuildRequires:  ruby3.3
%endif
%if %{with ruby34}
BuildRequires:  ruby3.4
%endif
%if %{with ruby35}
BuildRequires:  ruby3.5
%endif
%if %{with ruby40}
BuildRequires:  ruby4.0
%endif
BuildRequires:  ruby-macros >= 5
%if %{with gem2rpm_bootstrap}
#!BuildIgnore:  rubygem(gem2rpm) rubygem(ruby:2.1.0:gem2rpm) rubygem(ruby:2.2.0:gem2rpm) rubygem(rbx:2.2:gem2rpm)
%else
BuildRequires:  %{rubygem gem2rpm}
%endif
BuildRequires:  ruby-common >= 3.2
BuildRequires:  update-alternatives
URL:            https://github.com/lutter/gem2rpm/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        update-suse-patch.sh
Source2:        gem2rpm-opensuse
Source3:        series
Patch01:        suse.patch
Summary:        Generate rpm specfiles from gems
License:        GPL-2.0-or-later
Group:          Development/Languages/Ruby

%description
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%prep
%gem_unpack
%autopatch -p1

%build
perl -p -i -e 's|("templates/opensuse.spec.erb".freeze)|$1, "templates/gem_packages.spec.erb".freeze|g' *gemspec
%gem_build

%install
%gem_install -f -N --symlink-binaries --doc-files="AUTHORS LICENSE README"
for i in %{buildroot}%{_docdir}/*rubygem-gem2rpm*/ ; do
  install -m 0644 gem2rpm-%{version}/gem2rpm.yml.documentation $i/gem2rpm.yml
done

%if %{with gem2rpm_bootstrap}
%if %{with ruby21}
%package -n ruby2.1-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.1-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.1-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.1-rubygem-gem2rpm = %{version}

%description -n ruby2.1-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.1-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.1-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.1-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.1 gem2rpm.ruby2.1 %{_bindir}/gem2rpm.ruby2.1-%{version} %{mod_weight}

%preun -n ruby2.1-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.1-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.1-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.1  %{_bindir}/gem2rpm.ruby2.1-%{version}
fi

%files -n ruby2.1-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.1-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.1-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.1
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.1
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.1.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.1.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.1.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.1-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.1.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby25}
%package -n ruby2.5-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby2.5-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby2.5-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby2.5-rubygem-gem2rpm = %{version}

%description -n ruby2.5-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby2.5-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby2.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby2.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby2.5 gem2rpm.ruby2.5 %{_bindir}/gem2rpm.ruby2.5-%{version} %{mod_weight}

%preun -n ruby2.5-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby2.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby2.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby2.5  %{_bindir}/gem2rpm.ruby2.5-%{version}
fi

%files -n ruby2.5-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby2.5-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby2.5-%{version}
%ghost %{_bindir}/gem2rpm.ruby2.5
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby2.5
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/2.5.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/2.5.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/2.5.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby2.5-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/2.5.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby32}
%package -n ruby3.2-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.2-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.2-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.2-rubygem-gem2rpm = %{version}

%description -n ruby3.2-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.2-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.2-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.2-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.2 gem2rpm.ruby3.2 %{_bindir}/gem2rpm.ruby3.2-%{version} %{mod_weight}

%preun -n ruby3.2-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.2-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.2-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.2  %{_bindir}/gem2rpm.ruby3.2-%{version}
fi

%files -n ruby3.2-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.2-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.2-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.2
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.2
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.2.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.2.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.2.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.2-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.2.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby33}
%package -n ruby3.3-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.3-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.3-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.3-rubygem-gem2rpm = %{version}

%description -n ruby3.3-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.3-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.3-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.3-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.3 gem2rpm.ruby3.3 %{_bindir}/gem2rpm.ruby3.3-%{version} %{mod_weight}

%preun -n ruby3.3-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.3-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.3-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.3  %{_bindir}/gem2rpm.ruby3.3-%{version}
fi

%files -n ruby3.3-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.3-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.3-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.3
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.3
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.3.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.3.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.3.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.3-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.3.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby34}
%package -n ruby3.4-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.4-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.4-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.4-rubygem-gem2rpm = %{version}

%description -n ruby3.4-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.4-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.4-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.4-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.4 gem2rpm.ruby3.4 %{_bindir}/gem2rpm.ruby3.4-%{version} %{mod_weight}

%preun -n ruby3.4-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.4-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.4-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.4  %{_bindir}/gem2rpm.ruby3.4-%{version}
fi

%files -n ruby3.4-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.4-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.4-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.4
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.4
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/3.4.0/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/3.4.0/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/3.4.0/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.4-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/3.4.0/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby35}
%define rb_350_abi 3.5.0+0

%package -n ruby3.5-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby3.5-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby3.5-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby3.5-rubygem-gem2rpm = %{version}

%description -n ruby3.5-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby3.5-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby3.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby3.5-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby3.5 gem2rpm.ruby3.5 %{_bindir}/gem2rpm.ruby3.5-%{version} %{mod_weight}

%preun -n ruby3.5-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby3.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby3.5-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby3.5  %{_bindir}/gem2rpm.ruby3.5-%{version}
fi

%files -n ruby3.5-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby3.5-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby3.5-%{version}
%ghost %{_bindir}/gem2rpm.ruby3.5
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby3.5
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/%{rb_350_abi}/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/%{rb_350_abi}/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/%{rb_350_abi}/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby3.5-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/%{rb_350_abi}/doc/gem2rpm-%{version}
%endif
%endif

%if %{with ruby40}
%define rb_400_abi 4.0.0

%package -n ruby4.0-rubygem-gem2rpm
Summary:        Generate rpm specfiles from gems
Group:          Development/Languages/Ruby
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n ruby4.0-rubygem-gem2rpm
Generate source rpms and rpm spec files from a Ruby Gem.
The spec file tries to follow the gem as closely as possible

%package -n ruby4.0-rubygem-gem2rpm-doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       ruby4.0-rubygem-gem2rpm = %{version}

%description -n ruby4.0-rubygem-gem2rpm-doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%post -n ruby4.0-rubygem-gem2rpm
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm         gem2rpm         %{_bindir}/gem2rpm.ruby4.0-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm-%{version}   gem2rpm-%{version}   %{_bindir}/gem2rpm.ruby4.0-%{version} %{mod_weight}
/usr/sbin/update-alternatives --install \
    %{_bindir}/gem2rpm.ruby4.0 gem2rpm.ruby4.0 %{_bindir}/gem2rpm.ruby4.0-%{version} %{mod_weight}

%preun -n ruby4.0-rubygem-gem2rpm
if [ "$1" = 0 ] ; then
    /usr/sbin/update-alternatives --remove gem2rpm          %{_bindir}/gem2rpm.ruby4.0-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm-%{version}    %{_bindir}/gem2rpm.ruby4.0-%{version}
    /usr/sbin/update-alternatives --remove gem2rpm.ruby4.0  %{_bindir}/gem2rpm.ruby4.0-%{version}
fi

%files -n ruby4.0-rubygem-gem2rpm
%defattr(-,root,root,-)
%{_docdir}/ruby4.0-rubygem-gem2rpm
#{_bindir}/gem2rpm-opensuse
%{_bindir}/gem2rpm.ruby4.0-%{version}
%ghost %{_bindir}/gem2rpm.ruby4.0
%ghost %{_bindir}/gem2rpm-%{version}
%ghost %{_bindir}/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm
%ghost %{_sysconfdir}/alternatives/gem2rpm.ruby4.0
%ghost %{_sysconfdir}/alternatives/gem2rpm-%{version}
# cache file
%{_libdir}/ruby/gems/%{rb_400_abi}/cache/gem2rpm-%{version}.gem
%{_libdir}/ruby/gems/%{rb_400_abi}/gems/gem2rpm-%{version}
%{_libdir}/ruby/gems/%{rb_400_abi}/specifications/gem2rpm-%{version}.gemspec

%if %{with docs}
%files -n ruby4.0-rubygem-gem2rpm-doc
%defattr(-,root,root,-)
%doc %{_libdir}/ruby/gems/%{rb_400_abi}/doc/gem2rpm-%{version}
%endif
%endif

%else
%gem_packages
%endif

%changelog
