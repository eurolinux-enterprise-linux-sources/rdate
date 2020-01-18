Summary: Tool for getting the date/time from a remote machine
Name: rdate
Version: 1.4
Release: 25%{?dist}
License: GPLv2+
Group: Applications/System
Source: ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.gz
Patch0: rdate-1.4-udp.patch
Patch1: rdate-1.4-addrinfo.patch
Patch2: rdate-1.4-spellerr.patch
Patch3: rdate-1.4-memleak.patch
URL: ftp://people.redhat.com/sopwith/

%description
The rdate utility retrieves the date and time from another machine on
your network, using the protocol described in RFC 868. If you run
rdate as root, it will set your machine's local time to the time of
the machine that you queried.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DINET6 -fno-strict-aliasing"

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
make prefix=$RPM_BUILD_ROOT/usr install

%files
%doc COPYING
%attr(0755,root,root) %{_bindir}/rdate
%{_mandir}/man1/rdate.1*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.4-25
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-24
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Honza Horak <hhorak@redhat.com> - 1.4-22
- Added -fno-strict-aliasing to cflags

* Tue Sep 18 2012 Honza Horak <hhorak@redhat.com> - 1.4-21
- Minor spec file fixes

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Honza Horak <hhorak@redhat.com> - 1.4-19
- Fixed a memory leak
  Resolves: #800493

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Honza Horak <hhorak@redhat.com> - 1.4-16
- man page fix

* Fri Feb 26 2010 Jiri Moskovcak <jmoskovc@redhat.com> - 1.4-15
- added COPYING

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-12
- fix license tag

* Mon Mar 31 2008 Jiri Moskovcak <jmoskovc@redhat.com> - 1.4-11
- fixed early freeing of addrinfo

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4-10
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.4-9
- Rebuild for selinux ppc32 issue.

* Tue Jul 10 2007 Jiri Moskovcak <jmoskovc@redhat.com> 1.4-8
- fixes memory allocation
- Resolves: #190883

* Tue May 29 2007 Phil Knirsch <pknirsch@redhat.com> - 1.4-7
- Ceanups related to package review. (#226357)

* Fri Aug 25 2006 Phil Knirsch <pknirsch@redhat.com> - 1.4-6
- Enabled IPv6 support (#197509)

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 1.4-5
- bump

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.4-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.4-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 1.4-4
- bump release and rebuild with gcc 4

* Fri Feb 18 2005 Phil Knirsch <pknirsch@redhat.com> 1.4-3
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com> 1.4-2
- rebuilt

* Mon Mar 22 2004 Elliot Lee <sopwith@redhat.com> 1.4-1
- Timeout (-t) patch from Johan Nilsson <joh-nils@dsv.su.se>

* Wed Jan 29 2003 Phil Knirsch <pknirsch@redhat.com> 1.3-2
- Bump release and rebuild.

* Wed Nov 06 2002 Elliot Lee <sopwith@redhat.com> 1.3-1
- New release

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Phil Knirsch <pknirsch@redhat.com> 1.2-4
- Don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Mar 07 2002 Elliot Lee <sopwith@redhat.com>
- Make a 1.2 release, update to it. In the future, please commit changes
to CVS and make a new release, instead of adding patches to the rpm
package.

* Mon Feb 25 2002 Elliot Lee <sopwith@redhat.com>
- Bump & rebuild for 7.3

* Wed Dec  5 2001 Tim Powers <timp@redhat.com>
- bump release number and rebuild on alpha.

* Thu Dec  7 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Fixed Bugzilla bug #41119. More of a RFE, but still important.

* Thu Dec  7 2000 Crutcher Dunnavant <crutcher@redhat.com>
- rebuild for new tree

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- summaries from specspo.

* Wed Aug 09 2000 Philipp Knirsch <pknirsch@redhat.com>
- Bugfix for missing /etc/services entry for time protocol (#15797)

* Mon Jul 31 2000 Crutcher Dunnavant <crutcher@redhat.com>
- tracked successful rdate attempts, so that failure returns 1

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Fri Feb 04 2000 Elliot Lee <sopwith@redhat.com>
- Rewrite the stinking thing due to license worries (bug #8619)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- fixed the url to the source

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
