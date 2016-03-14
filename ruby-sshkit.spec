#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	sshkit
Summary:	SSHKit makes it easy to write structured, testable SSH commands in Ruby
Name:		ruby-%{pkgname}
Version:	1.9.0
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	4eb808cf5a4ac954328fdc1965f5e232
URL:		http://github.com/capistrano/sshkit
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest >= 5.0.0
BuildRequires:	ruby-minitest-reporters
BuildRequires:	ruby-mocha
BuildRequires:	ruby-rake
BuildRequires:	ruby-rubocop
BuildRequires:	ruby-unindent
%endif
Requires:	ruby-net-scp >= 1.1.2
Requires:	ruby-net-ssh >= 2.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A comprehensive toolkit for remotely running commands in a structured
manner on groups of servers.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%dir %{ruby_vendorlibdir}/core_ext
%{ruby_vendorlibdir}/core_ext/array.rb
%{ruby_vendorlibdir}/core_ext/hash.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
