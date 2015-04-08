##
## rpmbuild --define "srcdir elements" --define "inst tfel0" --define "artifact_version 1.88-SNAPSHOT" --define "relmajmin t" --define "buildver 1088" -ba lg-elements-core.spec
##

%define _rpmdir                     %{_topdir}/RPMS/software/Livegamer-Software-Release
%define __os_install_post           %{nil}
%define jboss_version               4.2.3.GA-1
%define jboss_root                  /opt/jboss/jboss-%{jboss_version}
%define inst_root                   server/%{inst}

Name:       sw-libra-%{inst}
Summary:    Eric Test Project
Version:    %{relmajmin}.%{buildver}
Release:    1
BuildArch:  noarch
License:    Proprietary
Vendor:     Live Gamer, Inc.
Group:      Application
BuildRoot:  %{_tmppath}/%{name}-%{relmajmin}-%{release}-build

%description
Twofish Elements

%pre
/usr/bin/id -g %{inst} >/dev/null 2>&1 || /usr/sbin/groupadd %{inst} >/dev/null 2>&1
/usr/bin/id %{inst} >/dev/null 2>&1 || /usr/sbin/useradd %{inst} -c "JBoss %{inst}" -g %{inst} >/dev/null 2>&1

%prep
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{_rpmdir}

%install
%{__mkdir} -p %{buildroot}/%{jboss_root}/%{inst_root}
%{__mkdir} -p %{buildroot}/%{jboss_root}/%{inst_root}/deploy
%{__mkdir} -p %{buildroot}/%{jboss_root}/%{inst_root}/lib
%{__cp} %{srcdir}/target/libra-%{artifact_version}.jar  %{buildroot}/%{jboss_root}/%{inst_root}/deploy/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,%{inst},%{inst})
%dir %{jboss_root}/%{inst_root}
%dir %{jboss_root}/%{inst_root}/deploy
     %{jboss_root}/%{inst_root}/deploy/libra-%{artifact_version}.jar

%changelog
* Mon Sep 25 2012 - scott@livegamer.com
- Changed artifacts to match new maven build
* Mon Aug 20 2012 - mau@livegamer.com
- Removed linehandler.properties
* Wed Mar 16 2011 - bmathiyakom@livegamer.com
- Branched for sprint 54
* Sun Aug 22 2010 - bmathiyakom@livegamer.com
- Add bulk service
* Thu May 27 2010 - albert@twofish.com
- Added monitoring-1.0.0.ear and monitoring-1.0.0.jar 
* Tue May 24 2010 - doug@twofish.com
- Added zstartup-1.0.0.ear and zstartup-1.0.0.jar
* Wed Mar 17 2010 - doug@twofish.com
- Added linehandler.properties
* Sun Nov 10 2009 - doug@twofish.com
- Initial version
