OasisLMF Changelog
==================

`2.4.5`_
 ---------
* [#1729](https://github.com/OasisLMF/OasisLMF/pull/1729) - Combus type fix
* [#1724](https://github.com/OasisLMF/OasisLMF/pull/1730) - add oed group fields to summary report
* [#1731](https://github.com/OasisLMF/OasisLMF/pull/1731) - Update README minimum python version to 3.9
* [#1699](https://github.com/OasisLMF/OasisLMF/pull/1702) - Error when requesting only ground-up losses by AccName
* [#1707](https://github.com/OasisLMF/OasisLMF/pull/1708) - Dynamic footprint - confluences
* [#1688](https://github.com/OasisLMF/OasisLMF/pull/1712) - Type 2 losses increasing differences when including secondary perils
* [#1713](https://github.com/OasisLMF/OasisLMF/pull/1713) - add forgotten fm test unit
* [#1715](https://github.com/OasisLMF/OasisLMF/pull/1715) - fix/lecpy `bin` tests assert equality with rounding
* [#1466](https://github.com/OasisLMF/OasisLMF/pull/1716) - Pandas 2.2.0 and up generates inconsistent results 
* [#1714, #1711](https://github.com/OasisLMF/OasisLMF/pull/1717) - fix level_id when an extra account level is needed
* [#1718](https://github.com/OasisLMF/OasisLMF/pull/1718) - remove empty cdf bin
* [#1691](https://github.com/OasisLMF/OasisLMF/pull/1722) - Added disaggregated locations info to exposure summary
* [#1723](https://github.com/OasisLMF/OasisLMF/pull/1723) - use pd explode to split peril covered columns
.. _`2.4.5`:  https://github.com/OasisLMF/OasisLMF/compare/2.4.4...2.4.5

`2.4.4`_
 ---------
* [#1697](https://github.com/OasisLMF/OasisLMF/pull/1697) - feature/dynamic_multiperil
* [#1701](https://github.com/OasisLMF/OasisLMF/pull/1701) - Combus repo origin/combus fix sampling
* [#1569](https://github.com/OasisLMF/OasisLMF/pull/1606) - Standardised model documentation 
* [#1666](https://github.com/OasisLMF/OasisLMF/pull/1683) - Support parquet for new pytools
* [#1690](https://github.com/OasisLMF/OasisLMF/pull/1690) - support uploading byte stream
* [#1656](https://github.com/OasisLMF/OasisLMF/pull/1658) - Step policies with peril-specific terms
* [#1695](https://github.com/OasisLMF/OasisLMF/pull/1694) - mock url for forex_python in test cases needs to be updated
.. _`2.4.4`:  https://github.com/OasisLMF/OasisLMF/compare/2.4.3...2.4.4

`2.4.3`_
 ---------
* [#1667](https://github.com/OasisLMF/OasisLMF/pull/1667) - add keys in error for loc_id not modelled
* [#1669](https://github.com/OasisLMF/OasisLMF/pull/1668) - Pytools Optimisations
* [#1672](https://github.com/OasisLMF/OasisLMF/pull/1672) - eltpy sum loss and sum loss square need to be float64 to avoid to much precision error
* [#1613](https://github.com/OasisLMF/OasisLMF/pull/1673) - Support output of results grouped as Property Damage (PD)
* [#1671](https://github.com/OasisLMF/OasisLMF/pull/1676) - Vulnerability blending optimisation
* [#1685](https://github.com/OasisLMF/OasisLMF/pull/1685) - Fixed health check exception on api connect
.. _`2.4.3`:  https://github.com/OasisLMF/OasisLMF/compare/2.4.2...2.4.3

`2.4.2`_
 ---------
* [#1665](https://github.com/OasisLMF/OasisLMF/pull/1665) - add support for geotiff in buildin lookup
* [#1527](https://github.com/OasisLMF/OasisLMF/pull/1636) - Add summary descriptions to output files
* [#1637](https://github.com/OasisLMF/OasisLMF/pull/1637) -   Z-order Indexing
* [#1610](https://github.com/OasisLMF/OasisLMF/pull/1610) - Feature/lecpy
* [#1608](https://github.com/OasisLMF/OasisLMF/pull/1646) - pytools kat
* [#1648](https://github.com/OasisLMF/OasisLMF/pull/1648) - in fm add polnumber information to level with no terms
* [#1649](https://github.com/OasisLMF/OasisLMF/pull/1649) - Non-NumBa Error Logging
* [#1650](https://github.com/OasisLMF/OasisLMF/pull/1650) - Fix for Platform V2 repairing run dir 
* [#1652](https://github.com/OasisLMF/OasisLMF/pull/1652) - Fix workaround for failing data null string tests 
* [#1653](https://github.com/OasisLMF/OasisLMF/pull/1653) - fix for  empty geopandas df sjoin not supported in geopandas 1.x
* [#1655](https://github.com/OasisLMF/OasisLMF/pull/1654) - Vulnerability blending feature performance tuning
.. _`2.4.2`:  https://github.com/OasisLMF/OasisLMF/compare/2.4.1...2.4.2

`2.4.1`_
 ---------
* [#1629](https://github.com/OasisLMF/OasisLMF/pull/1632) - Add computaion schema to CI and update documentaion
* [#1604](https://github.com/OasisLMF/OasisLMF/pull/1633) - exposure run crashes if CondPeril is missing
* [#1634](https://github.com/OasisLMF/OasisLMF/pull/1634) - Update release section in readme
* [#1603](https://github.com/OasisLMF/OasisLMF/pull/1603) - Feature/aalpy
* [#1573](https://github.com/OasisLMF/OasisLMF/pull/1635) - Update or Remove preparation/oed.py
* [#1638](https://github.com/OasisLMF/OasisLMF/pull/1638) - CI Fix, Skip incompatible client checks 
* [#1528](https://github.com/OasisLMF/OasisLMF/pull/1579) - Output Calc Python Rewrite
* [#1528](https://github.com/OasisLMF/OasisLMF/pull/1590) - Output Calc Python Rewrite
* [#1628](https://github.com/OasisLMF/OasisLMF/pull/1628) - Update pages workflow
* [#1630](https://github.com/OasisLMF/OasisLMF/pull/1630) - fix issue with loc id
* [#1631](https://github.com/OasisLMF/OasisLMF/pull/1631) - specify parquet folder to improve footprint read time
.. _`2.4.1`:  https://github.com/OasisLMF/OasisLMF/compare/2.4.0...2.4.1

`2.4.0`_
 ---------
* [#1394](https://github.com/OasisLMF/OasisLMF/pull/1601) - Net RI losses do not use -z in summarycalc
* [#1607](https://github.com/OasisLMF/OasisLMF/pull/1607) - Fix/lookup sort keys
* [#1591](https://github.com/OasisLMF/OasisLMF/pull/1592) - Dynamic footprint has incorrect type 1 losses
* [#1611](https://github.com/OasisLMF/OasisLMF/pull/1611) - fix loss_out len in account level back allocation
* [#1615](https://github.com/OasisLMF/OasisLMF/pull/1614) - Non-useful error message for missing PolInceptionDate with RA Basis reinsurance
* [#1552](https://github.com/OasisLMF/OasisLMF/pull/1552) - Make analysis and model setting able to modify any computation step parameters (MDK parameters)
* [#1618](https://github.com/OasisLMF/OasisLMF/pull/1618) - Fix testing failures (API Client) 
* [#1619](https://github.com/OasisLMF/OasisLMF/pull/1619) - Fix/ci pre analysis testing
* [#1624](https://github.com/OasisLMF/OasisLMF/pull/1624) - Feature/oed v4
* [#1625](https://github.com/OasisLMF/OasisLMF/pull/1625) - feat: security enhancements
.. _`2.4.0`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.11...2.4.0

`2.3.11`_
 ---------
* [#1394](https://github.com/OasisLMF/OasisLMF/pull/1601) - Net RI losses do not use -z in summarycalc
* [#1250](https://github.com/OasisLMF/OasisLMF/pull/1576) - Support Risk Attaching 'RA' basis in reinsurance
* [#1581](https://github.com/OasisLMF/OasisLMF/pull/1587) - oasislmf code uses legacy correlation settings location in model settings
* [#1589](https://github.com/OasisLMF/OasisLMF/pull/1589) - Update platform API client for Cyber models 
* [#1594](https://github.com/OasisLMF/OasisLMF/pull/1594) - improve the memory performance of il layer number continuity step
* [#1595](https://github.com/OasisLMF/OasisLMF/pull/1596) - Allow process perils with different resolution grids 
.. _`2.3.11`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.10...2.3.11

`2.3.10`_
 ---------
* [#1563](https://github.com/OasisLMF/OasisLMF/pull/1570) - Intensity Adjustments in gulmc for dynamic footprints
* [#1572](https://github.com/OasisLMF/OasisLMF/pull/1572) - Release 2.3.9
* [#1585, #1575](https://github.com/OasisLMF/OasisLMF/pull/1574) - Fix missing complex keys return without amplification
* [#1578](https://github.com/OasisLMF/OasisLMF/pull/1578) - fix: point to the correct source in error message for vulnerabiity_id…
* [#1580](https://github.com/OasisLMF/OasisLMF/pull/1584) - Hazard correlation defaults to 100% if missing
* [#1581](https://github.com/OasisLMF/OasisLMF/pull/1587) - oasislmf code uses legacy correlation settings location in model settings
.. _`2.3.10`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.9...2.3.10

`2.3.9`_
 ---------
* [#1567](https://github.com/OasisLMF/OasisLMF/pull/1568) - Occurrence file not found when requesting output from ktools component alt_meanonly
* [#1563](https://github.com/OasisLMF/OasisLMF/pull/1570) - Intensity Adjustments in gulmc for dynamic footprints
* [#1379](https://github.com/OasisLMF/OasisLMF/pull/1550) - Performance issue in get_exposure_summary
* [#1557](https://github.com/OasisLMF/OasisLMF/pull/1557) - Release 2.3.8
* [#1558](https://github.com/OasisLMF/OasisLMF/pull/1558) - support for having several pla sets
* [#1560](https://github.com/OasisLMF/OasisLMF/pull/1560) - add check for vulnerability id and intensity bin boundary
* [#1566](https://github.com/OasisLMF/OasisLMF/pull/1565) - Fiona package vulnerability issue
.. _`2.3.9`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.8...2.3.9

`2.3.8`_
 ---------
* [#1536](https://github.com/OasisLMF/OasisLMF/pull/1536) - Release 2.3.7 (Aug 6)
* [#1544](https://github.com/OasisLMF/OasisLMF/pull/1545) - dynamic footprint - slow performance for large hazard case
* [#1546](https://github.com/OasisLMF/OasisLMF/pull/1546) - Combus changes: 20240807
* [#1554](https://github.com/OasisLMF/OasisLMF/pull/1554) - drop duplicate il term lines before merging
* [#1547](https://github.com/OasisLMF/OasisLMF/pull/1555) - Running full_correlation + gulmc causes an execution to hang.  
* [#1556](https://github.com/OasisLMF/OasisLMF/pull/1556) - Fix CI build system failures 
* [#1559](https://github.com/OasisLMF/OasisLMF/pull/1559) - Read do_disaggregation from settings files
* [#1560](https://github.com/OasisLMF/OasisLMF/pull/1560) - add check for vulnerability id and intensity bin boundary
* [#1561](https://github.com/OasisLMF/OasisLMF/pull/1561) - Set Ktools 3.12.4
* [#1531](https://github.com/OasisLMF/OasisLMF/pull/1531) - fix effective deductible applied in minded calculation for calcrule 19
.. _`2.3.8`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.7...2.3.8

`2.3.7`_
 ---------
* [#1533](https://github.com/OasisLMF/OasisLMF/pull/1537) - API client names the downloaded output file .tar instead of .tar.gz
* [#1530](https://github.com/OasisLMF/OasisLMF/pull/1538) - Short flags unexpectedly changed in 2.3.6
* [#1539](https://github.com/OasisLMF/OasisLMF/pull/1540) - Allow keys files with both amplification_id and model_data columns
* [#1542](https://github.com/OasisLMF/OasisLMF/pull/1541) - Time and Memory performance issue for RI contract
* [#1523](https://github.com/OasisLMF/OasisLMF/pull/1523) - Release 2.3.6 (July 1st 2024)
* [#1531](https://github.com/OasisLMF/OasisLMF/pull/1531) - fix effective deductible applied in minded calculation for calcrule 19
* [#1532](https://github.com/OasisLMF/OasisLMF/pull/1532) - make all compute step run command oasis logged
* [#1468](https://github.com/OasisLMF/OasisLMF/pull/1534) - loss output at intermediate inuring priorities - new features 
* [#1535](https://github.com/OasisLMF/OasisLMF/pull/1535) - add interval mapping to built in function
.. _`2.3.7`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.6...2.3.7

`2.3.6`_
 ---------
* [#1516](https://github.com/OasisLMF/OasisLMF/pull/1516) - Added support for occurrence attachment for Per Risk XL
* [#1517](https://github.com/OasisLMF/OasisLMF/pull/1517) - event ranges
* [#1518](https://github.com/OasisLMF/OasisLMF/pull/1518) - Fix/pre analysis user dir
* [#1520, #1519](https://github.com/OasisLMF/OasisLMF/pull/1521) - get_vulns update
* [#1258](https://github.com/OasisLMF/OasisLMF/pull/1490) - Document oasislmf.json configuration options 
* [#1488](https://github.com/OasisLMF/OasisLMF/pull/1524) - Add post input-gen hook and pre exec hook
* [#1526](https://github.com/OasisLMF/OasisLMF/pull/1496) - Oasis Dynamic Model
* [#1529](https://github.com/OasisLMF/OasisLMF/pull/1529) - add user_data_dir to all the hooks
* [#1501](https://github.com/OasisLMF/OasisLMF/pull/1501) - Release 2.3.5 (30th May 2024)
.. _`2.3.6`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.5...2.3.6

`2.3.5`_
 ---------
* [#1503](https://github.com/OasisLMF/OasisLMF/pull/1504) - Add a guard which 'fast fails' runs using more than 9 summary groups + summarycalc 
* [#1454](https://github.com/OasisLMF/OasisLMF/pull/1505) - RI Scope file filters
* [#1506](https://github.com/OasisLMF/OasisLMF/pull/1507) - acc_idx read as category type from input/accounts.csv 
* [#1508](https://github.com/OasisLMF/OasisLMF/pull/1508) - fix pla reader
* [#1509](https://github.com/OasisLMF/OasisLMF/pull/1509) - improve perf of file preparation
* [#1510](https://github.com/OasisLMF/OasisLMF/pull/1510) - Fix error handling for failed file loading in 'get_dataframe'
* [#1498](https://github.com/OasisLMF/OasisLMF/pull/1513) - When LayerParticipation is not present, gross losses are not produced
* [#1489](https://github.com/OasisLMF/OasisLMF/pull/1489) - Release 2.3.4
* [#1491](https://github.com/OasisLMF/OasisLMF/pull/1494) - Correlation group fields are not generated correctly for disaggregated risks
* [#1499](https://github.com/OasisLMF/OasisLMF/pull/1500) - OASISLMF installation issue
.. _`2.3.5`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.4...2.3.5

`2.3.4`_
 ---------
* [#1476](https://github.com/OasisLMF/OasisLMF/pull/1476) - Release 2.3.2
* [#1480](https://github.com/OasisLMF/OasisLMF/pull/1480) -  Storage Manager fixes for Platform Lot3
* [#1481](https://github.com/OasisLMF/OasisLMF/pull/1481) - Set ktools to 3.12.1
* [#1487](https://github.com/OasisLMF/OasisLMF/pull/1482) - Remove or enable to change the limit of output summaries(currently set to 9)
* [#1355](https://github.com/OasisLMF/OasisLMF/pull/1486) - Refactor footprint file format priorities
.. _`2.3.4`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.2...2.3.4

`2.3.2`_
 ---------
* [#1471](https://github.com/OasisLMF/OasisLMF/pull/1472) - number_of_samples = 0 not working in oasislmf
* [#1473](https://github.com/OasisLMF/OasisLMF/pull/1473) - ajust vuln index after vuln_dict has the updated indexes
* [#1474](https://github.com/OasisLMF/OasisLMF/pull/1474) - Use billiard package for keys multiprocess if available
* [#1481](https://github.com/OasisLMF/OasisLMF/pull/1481) - Set ktools to 3.12.1
* [#1461](https://github.com/OasisLMF/OasisLMF/pull/1461) - Release 2.3.1
* [#1464](https://github.com/OasisLMF/OasisLMF/pull/1464) - Feature/add fm tests
* [#732](https://github.com/OasisLMF/OasisLMF/pull/1465) - Align FM and RI column headers 
.. _`2.3.2`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.1...2.3.2

`2.3.1`_
 ---------
* [#1444](https://github.com/OasisLMF/OasisLMF/pull/1444) - support for pandas 3
* [#1446](https://github.com/OasisLMF/OasisLMF/pull/1446) - Add missing loc_id check
* [#1447](https://github.com/OasisLMF/OasisLMF/pull/1447) - use correct error_model in back allocation
* [#1448](https://github.com/OasisLMF/OasisLMF/pull/1448) - ensure header is written in keys.csv
* [#1449](https://github.com/OasisLMF/OasisLMF/pull/1450) - Footprint_set option not working with parquet format
* [#1455](https://github.com/OasisLMF/OasisLMF/pull/1455) - fix for vuln parquet read
* [#1350](https://github.com/OasisLMF/OasisLMF/pull/1456) - model settings - correlation settings - allow optional hazard or damage correlation value 
* [#1445](https://github.com/OasisLMF/OasisLMF/pull/1457) - Platform API needs to check RUN_MODE to detect workflow  
* [#146](https://github.com/OasisLMF/OasisLMF/pull/1458) - Outputs Reinsurance: RI contract level output (by ReinsNumber and or ReinsType)
* [#1385](https://github.com/OasisLMF/OasisLMF/pull/1459) - Missing parquet library dependencies for gulmc in 1.27
* [#1460](https://github.com/OasisLMF/OasisLMF/pull/1463) - Occurrence file not found when requesting output from ktools component aalcalcmeanonly
* [#1467](https://github.com/OasisLMF/OasisLMF/pull/1467) - fix for 1 loc with no account fm terms
.. _`2.3.1`:  https://github.com/OasisLMF/OasisLMF/compare/2.3.0...2.3.1

`2.3.0`_
 ---------
* [#1409](https://github.com/OasisLMF/OasisLMF/pull/1409) - Fix server-version flag for API client runner
* [#1410](https://github.com/OasisLMF/OasisLMF/pull/1411) - Support for AccParticipation 
* [#1412](https://github.com/OasisLMF/OasisLMF/pull/1412) - use category for peril_id in keys.csv, improve write_fm_xref_file
* [#1413](https://github.com/OasisLMF/OasisLMF/pull/1413) - Release 1.28.5
* [#1408, #1414](https://github.com/OasisLMF/OasisLMF/pull/1415) - Replace single vulnerabilities through additional adjustments settings or file
* [#1416](https://github.com/OasisLMF/OasisLMF/pull/1416) - fix useful columns when extra aggregation level is needed
* [#1417](https://github.com/OasisLMF/OasisLMF/pull/1417) - Update CI job triggers - only test on PR or commit to main branches
* [#1418](https://github.com/OasisLMF/OasisLMF/pull/1418) - Set ktools to 3.11.1
* [#1421](https://github.com/OasisLMF/OasisLMF/pull/1421) - add test with location with 1 empty and 1 level 2 condtag
* [#1423](https://github.com/OasisLMF/OasisLMF/pull/1423) - add acc participation only
* [#1425](https://github.com/OasisLMF/OasisLMF/pull/1426) - Customise specific vulnerabilities (without providing full replacement data)
* [#140](https://github.com/OasisLMF/OasisLMF/pull/1299) - Implement OED peril fields
* [#1429](https://github.com/OasisLMF/OasisLMF/pull/1429) - franchise deductible
* [#1430](https://github.com/OasisLMF/OasisLMF/pull/1431) - FM acceptance tests failing with pandas==2.2.0 
* [#1422](https://github.com/OasisLMF/OasisLMF/pull/1432) - Adjust log levels separately for modules
* [#1435](https://github.com/OasisLMF/OasisLMF/pull/1435) - Fix/update defaults
* [#1441](https://github.com/OasisLMF/OasisLMF/pull/1441) - Feature/lot3 merge
* [#1443](https://github.com/OasisLMF/OasisLMF/pull/1443) - Set package versions for 2.3.0
* [#1249](https://github.com/OasisLMF/OasisLMF/pull/1320) - Discuss documentation strategy
* [#1324](https://github.com/OasisLMF/OasisLMF/pull/1324) - Release/1.28.0
* [#1334](https://github.com/OasisLMF/OasisLMF/pull/1334) - Update CI - 1.28
* [#1340](https://github.com/OasisLMF/OasisLMF/pull/1340) - collect_unused_df in il preparation
* [#1341](https://github.com/OasisLMF/OasisLMF/pull/1342) - Bug in latest platform2 release 
* [#1344](https://github.com/OasisLMF/OasisLMF/pull/1344) - Release/1.28.1 (staging) 
* [#1326](https://github.com/OasisLMF/OasisLMF/pull/1345) - Update the the `KeyLookupInterface` class to have access to the `lookup_complex_config_json`
* [#140](https://github.com/OasisLMF/OasisLMF/pull/1346) - Implement OED peril fields
* [#1349](https://github.com/OasisLMF/OasisLMF/pull/1349) - Fix removal of handlers to logger + give logfiles unique names
* [#1322](https://github.com/OasisLMF/OasisLMF/pull/1351) - Step policies: Allow BI ground up loss through to gross losses
* [#1293](https://github.com/OasisLMF/OasisLMF/pull/1352) - Multiple footprint file options
* [#1357](https://github.com/OasisLMF/OasisLMF/pull/1357) - fix permissions for docs deploy
* [#1360](https://github.com/OasisLMF/OasisLMF/pull/1360) - Add docs about gulmc
* [#1366](https://github.com/OasisLMF/OasisLMF/pull/1367) - Update fm supported terms document
* [#1347](https://github.com/OasisLMF/OasisLMF/pull/1369) - Add runtime user supplied secondary factor option to plapy
* [#1317](https://github.com/OasisLMF/OasisLMF/pull/1371) - Add post-analysis hook
* [#1372](https://github.com/OasisLMF/OasisLMF/pull/1373) - Incorect TIV in the summary info files
* [#1376](https://github.com/OasisLMF/OasisLMF/pull/1376) - Release 1.28.3
* [#1377](https://github.com/OasisLMF/OasisLMF/pull/1377) - Clean up 'runs' dir in repo
* [#1378](https://github.com/OasisLMF/OasisLMF/pull/1378) - Support output of overall average period loss without standard deviation calculation
* [#1292](https://github.com/OasisLMF/OasisLMF/pull/1380) - Parquet format summary info file
* [#1382](https://github.com/OasisLMF/OasisLMF/pull/1386) - Change vulnerability weight data type from 32-bit integer to 32-bit float in gulmc
* [#1387](https://github.com/OasisLMF/OasisLMF/pull/1387) - Release 1.28.4
* [#1381](https://github.com/OasisLMF/OasisLMF/pull/1388) - Converting exposure files to previous OED version before running model
* [#1394](https://github.com/OasisLMF/OasisLMF/pull/1397) - Net RI losses do not use -z in summarycalc
* [#1398](https://github.com/OasisLMF/OasisLMF/pull/1398) - Allow disaggregation to be disabled
* [#1399](https://github.com/OasisLMF/OasisLMF/pull/1399) - Fixed loading booleans from oasislmf.json
* [#1088](https://github.com/OasisLMF/OasisLMF/pull/1401) - Correlation options for the user
* [#1405](https://github.com/OasisLMF/OasisLMF/pull/1405) - Fix/non compulsory condtag
* [#1403](https://github.com/OasisLMF/OasisLMF/pull/1406) - Vulnerability File Option
* [#1407](https://github.com/OasisLMF/OasisLMF/pull/1407) - Added tests for condition coverages 1-5 financial terms
.. _`2.3.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.0...2.3.0

`1.28.5`_
 ---------
* [#1409](https://github.com/OasisLMF/OasisLMF/pull/1409) - Fix server-version flag for API client runner
* [#1410](https://github.com/OasisLMF/OasisLMF/pull/1411) - Support for AccParticipation
* [#1412](https://github.com/OasisLMF/OasisLMF/pull/1412) - use category for peril_id in keys.csv, improve write_fm_xref_file
* [#1416](https://github.com/OasisLMF/OasisLMF/pull/1416) - fix useful columns when extra aggregation level is needed
* [#1417](https://github.com/OasisLMF/OasisLMF/pull/1417) - Update CI job triggers - only test on PR or commit to main branches
* [#1418](https://github.com/OasisLMF/OasisLMF/pull/1418) - Set ktools to 3.11.1
* [#1347](https://github.com/OasisLMF/OasisLMF/pull/1369) - Add runtime user supplied secondary factor option to plapy
* [#1405](https://github.com/OasisLMF/OasisLMF/pull/1405) - Fix/non compulsory condtag
* [#1403](https://github.com/OasisLMF/OasisLMF/pull/1406) - Vulnerability File Option
* [#1407](https://github.com/OasisLMF/OasisLMF/pull/1407) - Added tests for condition coverages 1-5 financial terms
.. _`1.28.5`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.4...1.28.5

`1.28.4`_
 ---------
* [#1376](https://github.com/OasisLMF/OasisLMF/pull/1376) - Release 1.28.3
* [#1292](https://github.com/OasisLMF/OasisLMF/pull/1380) - Parquet format summary info file
* [#1382](https://github.com/OasisLMF/OasisLMF/pull/1386) - Change vulnerability weight data type from 32-bit integer to 32-bit float in gulmc
* [#1381](https://github.com/OasisLMF/OasisLMF/pull/1388) - Converting exposure files to previous OED version before running model
* [#140](https://github.com/OasisLMF/OasisLMF/pull/1299) - Implement OED peril fields
* [#1394](https://github.com/OasisLMF/OasisLMF/pull/1397) - Net RI losses do not use -z in summarycalc
* [#1398](https://github.com/OasisLMF/OasisLMF/pull/1398) - Allow disaggregation to be disabled
* [#1399](https://github.com/OasisLMF/OasisLMF/pull/1399) - Fixed loading booleans from oasislmf.json
* [#1347](https://github.com/OasisLMF/OasisLMF/pull/1369) - Add runtime user supplied secondary factor option to plapy
.. _`1.28.4`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.3...1.28.4

`1.28.3`_
 ---------
* [#1377](https://github.com/OasisLMF/OasisLMF/pull/1377) - Clean up 'runs' dir in repo
* [#1378](https://github.com/OasisLMF/OasisLMF/pull/1378) - Support output of overall average period loss without standard deviation calculation
* [#1366](https://github.com/OasisLMF/OasisLMF/pull/1367) - Update fm supported terms document
* [#1347](https://github.com/OasisLMF/OasisLMF/pull/1369) - Add runtime user supplied secondary factor option to plapy
* [#1317](https://github.com/OasisLMF/OasisLMF/pull/1371) - Add post-analysis hook
* [#1372](https://github.com/OasisLMF/OasisLMF/pull/1373) - Incorect TIV in the summary info files
.. _`1.28.3`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.2...1.28.3

`1.28.2`_
 ---------
* [#1344](https://github.com/OasisLMF/OasisLMF/pull/1344) - Release/1.28.1 (staging)
* [#1326](https://github.com/OasisLMF/OasisLMF/pull/1345) - Update the the `KeyLookupInterface` class to have access to the `lookup_complex_config_json`
* [#140](https://github.com/OasisLMF/OasisLMF/pull/1346) - Implement OED peril fields
* [#1322](https://github.com/OasisLMF/OasisLMF/pull/1351) - Step policies: Allow BI ground up loss through to gross losses
* [#1249](https://github.com/OasisLMF/OasisLMF/pull/1320) - Discuss documentation strategy
* [#1293](https://github.com/OasisLMF/OasisLMF/pull/1352) - Multiple footprint file options
* [#1357](https://github.com/OasisLMF/OasisLMF/pull/1357) - fix permissions for docs deploy
* [#1360](https://github.com/OasisLMF/OasisLMF/pull/1360) - Add docs about gulmc
* [#1347](https://github.com/OasisLMF/OasisLMF/pull/1369) - Add runtime user supplied secondary factor option to plapy
* [#1340](https://github.com/OasisLMF/OasisLMF/pull/1340) - collect_unused_df in il preparation
.. _`1.28.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.1...1.28.2

`1.28.1`_
 ---------
* [#1341](https://github.com/OasisLMF/OasisLMF/pull/1342) - Bug in latest platform2 release
* [#1324](https://github.com/OasisLMF/OasisLMF/pull/1324) - Release/1.28.0
* [#1349](https://github.com/OasisLMF/OasisLMF/pull/1349) - Fix removal of handlers to logger + give logfiles unique names
* [#1334](https://github.com/OasisLMF/OasisLMF/pull/1334) - Update CI - 1.28
.. _`1.28.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.0...1.28.1

`1.28.1rc1`_
 ---------
* [#1341](https://github.com/OasisLMF/OasisLMF/pull/1342) - Bug in latest platform2 release
* [#1324](https://github.com/OasisLMF/OasisLMF/pull/1324) - Release/1.28.0
* [#1349](https://github.com/OasisLMF/OasisLMF/pull/1349) - Fix removal of handlers to logger + give logfiles unique names
* [#1334](https://github.com/OasisLMF/OasisLMF/pull/1334) - Update CI - 1.28
.. _`1.28.1rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.28.0...1.28.1rc1

`1.28.0`_
 ---------
* [#1280](https://github.com/OasisLMF/OasisLMF/pull/1280) - Drop py3.7 in testing and add py3.11
* [#1134](https://github.com/OasisLMF/OasisLMF/pull/1153) - nan output in dummy model generated vulnerability file when intensity sparseness is low
* [#1282](https://github.com/OasisLMF/OasisLMF/pull/1282) - Adding tarfile member sanitization to extractall()
* [#1286](https://github.com/OasisLMF/OasisLMF/pull/1286) - Improve code coverage accuracy
* [#1288](https://github.com/OasisLMF/OasisLMF/pull/1287) - Support for pandas 2
* [#1289](https://github.com/OasisLMF/OasisLMF/pull/1289) - Fix/fillna on str
* [#1295](https://github.com/OasisLMF/OasisLMF/pull/1290) - Add platform client unit tests
* [#1291](https://github.com/OasisLMF/OasisLMF/pull/1291) - remove obsolete fm compute
* [#1294](https://github.com/OasisLMF/OasisLMF/pull/1294) - Removed obsolete Cookiecutter from oasislmf
* [#1296](https://github.com/OasisLMF/OasisLMF/pull/1296) - Pin ods-tools package for new fillna function
* [#1298](https://github.com/OasisLMF/OasisLMF/pull/1298) - Add testing for computation funcs
* [#1214](https://github.com/OasisLMF/OasisLMF/pull/1305) - Undefined behaviour when no successes are passed to write_oasis_keys_file
* [#1306](https://github.com/OasisLMF/OasisLMF/pull/1306) - lookup: remove extra column after failed combine step
* [#1307](https://github.com/OasisLMF/OasisLMF/pull/1308) - Update release section on Readme
* [#1156, #1180, #1151](https://github.com/OasisLMF/OasisLMF/pull/1181) - [gulmc] implement hazard correlation
* [#1310](https://github.com/OasisLMF/OasisLMF/pull/1310) - log wrapper, check log level before running input log
* [#902](https://github.com/OasisLMF/OasisLMF/pull/1309) - Support for monetary / absolute damage functions
* [#1315](https://github.com/OasisLMF/OasisLMF/pull/1315) - Bug fix for setcwd context manager
* [#1300](https://github.com/OasisLMF/OasisLMF/pull/1318) - Assignment of loc_id and idx is not unique when using an EPA to split locations across more rows
* [#1316](https://github.com/OasisLMF/OasisLMF/pull/1319) - Enhance pre-analysis hook
* [#1321](https://github.com/OasisLMF/OasisLMF/pull/1321) - Cleanup/fix fm validation cr
* [#1219](https://github.com/OasisLMF/OasisLMF/pull/1327) - Fix flakly checks in TestGetDataframe
* [#1142](https://github.com/OasisLMF/OasisLMF/pull/1328) - Post Loss Amplification
* [#1329](https://github.com/OasisLMF/OasisLMF/pull/1329) - Fix/ci skip ods build manual trigger
* [#1330](https://github.com/OasisLMF/OasisLMF/pull/1330) - Set Ktools to version 3.10.0
* [#1204](https://github.com/OasisLMF/OasisLMF/pull/1204) - Release/1.27.0
* [#1332](https://github.com/OasisLMF/OasisLMF/pull/1332) - fix correlation issue
* [#1207](https://github.com/OasisLMF/OasisLMF/pull/1209) - (FM) CondClass 1 as second priority condition doesn't work
* [#1211](https://github.com/OasisLMF/OasisLMF/pull/1212) - OSError: [Errno 24] Too many open files in gulmc test
* [#1218](https://github.com/OasisLMF/OasisLMF/pull/1218) - Fix missing default collumn for RI
* [#1220](https://github.com/OasisLMF/OasisLMF/pull/1220) - Fix mapping of `vuln_idx` to `vuln_i` and implement `eff_vuln_cdf` as a dynamic array to work with large footprints
* [#1222](https://github.com/OasisLMF/OasisLMF/pull/1222) - add option to have custom oed schema
* [#1230](https://github.com/OasisLMF/OasisLMF/pull/1229) - Redirect warnings from pytools
* [#1231](https://github.com/OasisLMF/OasisLMF/pull/1231) - Fix expecteted output with Extra TIV cols from ods-tools
* [#1232](https://github.com/OasisLMF/OasisLMF/pull/1232) - Moved Settings JSON validation to ods-tools
* [#1233](https://github.com/OasisLMF/OasisLMF/pull/1234) - oasislmf exposure run reports missing location file when account missing
* [#141](https://github.com/OasisLMF/OasisLMF/pull/1235) - Implement account level financial structures
* [#1236](https://github.com/OasisLMF/OasisLMF/pull/1236) - Switch changelog builder from "build" repo to "OasisPlatform"
* [#1237](https://github.com/OasisLMF/OasisLMF/pull/1237) - Add *.npy to gitignore and clean files from validation
* [#1238](https://github.com/OasisLMF/OasisLMF/pull/1238) - Set oasislmf to version 1.27.2
* [#1245](https://github.com/OasisLMF/OasisLMF/pull/1242) - Add the possibility to have both policy coverage and policy PD
* [#28](https://github.com/OasisLMF/OasisLMF/pull/1243) - Fix/genbash
* [#1244](https://github.com/OasisLMF/OasisLMF/pull/1244) - Use console entrypoint to define and install `oasislmf` binary
* [#1251](https://github.com/OasisLMF/OasisLMF/pull/1252) - Error caused by pandas 2.0.0
* [#1247](https://github.com/OasisLMF/OasisLMF/pull/1255) - OED/oasislmf version compatibility matrix #oasislmf
* [#1253](https://github.com/OasisLMF/OasisLMF/pull/1256) - pandas 2.0.0 error using "oed_fields" in analysis settings
* [#1257](https://github.com/OasisLMF/OasisLMF/pull/1257) - Fix summary levels file
* [#1130](https://github.com/OasisLMF/OasisLMF/pull/1130) - Remove check for IL + RI files from the run model cmd
* [#1260](https://github.com/OasisLMF/OasisLMF/pull/1260) - Use low_memory=False in get_dataframe
* [#1123](https://github.com/OasisLMF/OasisLMF/pull/1261) - Stochastic disaggregation 4 & 6 File preparation for disaggregated locations
* [#1259](https://github.com/OasisLMF/OasisLMF/pull/1262) - Duplicate summary_ids in outputs
* [#1221](https://github.com/OasisLMF/OasisLMF/pull/1265) - Enable simple way to specify hierarchal key lookup in lookup_config.json
* [#1267](https://github.com/OasisLMF/OasisLMF/pull/1269) - Numba 0.57 breaks fmpy
* [#1270](https://github.com/OasisLMF/OasisLMF/pull/1270) - Add generate and run to rest client
* [#1272](https://github.com/OasisLMF/OasisLMF/pull/1272) - Update numpy pin
* [#1277](https://github.com/OasisLMF/OasisLMF/pull/1277) - Fix invalid columns in FM tests
.. _`1.28.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.27.0...1.28.0

`1.27.0`_
 ---------
* [#135](https://github.com/OasisLMF/OasisLMF/pull/1024) - Implement OED policy coverage terms in Financial Module
* [#1154](https://github.com/OasisLMF/OasisLMF/pull/1154) - Update `.gitignore`
* [#1157](https://github.com/OasisLMF/OasisLMF/pull/1157) - Fix fm visualizer tool
* [#1160](https://github.com/OasisLMF/OasisLMF/pull/1160) - Don't write temp files during test
* [#1198](https://github.com/OasisLMF/OasisLMF/pull/1198) - Fix/pep8-code-quality-pr-trigger
* [#1165](https://github.com/OasisLMF/OasisLMF/pull/1165) - Hotfix/update piwind tests
* [#1169](https://github.com/OasisLMF/OasisLMF/pull/1167) - Track code coverage
* [#1188, #1126](https://github.com/OasisLMF/OasisLMF/pull/1168) - Implement weighted vulnerability feature in `gulmc`
* [#1201](https://github.com/OasisLMF/OasisLMF/pull/1199) - Update/add necessary docstrings in `gulmc`
* [#1169](https://github.com/OasisLMF/OasisLMF/pull/1170) - Track code coverage
* [#908](https://github.com/OasisLMF/OasisLMF/pull/1171) - ensure that logging is sufficient to capture and report all common errors
* [#1174](https://github.com/OasisLMF/OasisLMF/pull/1174) - Set pip-compile to backtracking and trim unused requirments
* [#1175](https://github.com/OasisLMF/OasisLMF/pull/1175) - Fix drop na in expected data
* [#1176](https://github.com/OasisLMF/OasisLMF/pull/1176) - Feature/ods tools migration test
* [#1177](https://github.com/OasisLMF/OasisLMF/pull/1179) - The run_ktools.sh script does not check if all custom gulcalc processes completed successfully.
* [#1182](https://github.com/OasisLMF/OasisLMF/pull/1182) - Feature/ods tools migration piwind fix
* [#1048](https://github.com/OasisLMF/OasisLMF/pull/1055) - set modelpy and gulpy as default runtime options
* [#1057](https://github.com/OasisLMF/OasisLMF/pull/1057) - Remove sys.exit(1) calls and replace with exceptions
* [#1058](https://github.com/OasisLMF/OasisLMF/pull/1058) - Correlation map
* [#1187](https://github.com/OasisLMF/OasisLMF/pull/1186) - `sklearn` is now deprecated in requirements files: use `scikit-learn` instead
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1060) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1040](https://github.com/OasisLMF/OasisLMF/pull/1062) - Builtin lookup - missing feedback when all locations are using unsupported LocPerilsCovered
* [#1063](https://github.com/OasisLMF/OasisLMF/pull/1063) - Fix/pre analysis hook
* [#1007](https://github.com/OasisLMF/OasisLMF/pull/1064) - Parquet to csv comparison script
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1065) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1191](https://github.com/OasisLMF/OasisLMF/pull/1194) - Github actions to manage new issues and PR's
* [#1067](https://github.com/OasisLMF/OasisLMF/pull/1067) - Fix/platform run
* [#1184](https://github.com/OasisLMF/OasisLMF/pull/1193) - Add `gulmc` option to the model runner
* [#1068](https://github.com/OasisLMF/OasisLMF/pull/1069) - Implement correlated random number generation in gulpy
* [#1192](https://github.com/OasisLMF/OasisLMF/pull/1192) - Track pid of gulcalc processes and wait on them in `run_ktools.sh`
* [#1071](https://github.com/OasisLMF/OasisLMF/pull/1071) - Feature/param loading
* [#1072](https://github.com/OasisLMF/OasisLMF/pull/1072) - Update/package requirements
* [#1070](https://github.com/OasisLMF/OasisLMF/pull/1073) - Clean up warning messages
* [#1074](https://github.com/OasisLMF/OasisLMF/pull/1074) - Added lower-case-cols and raise-error flags
* [#1075](https://github.com/OasisLMF/OasisLMF/pull/1075) - setting model_custom_gulcalc disables gulpy
* [#1076](https://github.com/OasisLMF/OasisLMF/pull/1076) - Set ktools to 3.9.2
* [#992](https://github.com/OasisLMF/OasisLMF/pull/1077) - Peril Specific Runs
* [#1049](https://github.com/OasisLMF/OasisLMF/pull/1078) - random number generator can be set to 0 at oasislmf command line
* [#1066](https://github.com/OasisLMF/OasisLMF/pull/1079) - Gulpy failing in distributed runs
* [#1080](https://github.com/OasisLMF/OasisLMF/pull/1080) - add peril_filter to run settings spec
* [#1200](https://github.com/OasisLMF/OasisLMF/pull/1200) - Update CI badges
* [#1016](https://github.com/OasisLMF/OasisLMF/pull/1082) - Update package testing
* [#1203](https://github.com/OasisLMF/OasisLMF/pull/1203) - Update Develop to be inline with master
* [#1085](https://github.com/OasisLMF/OasisLMF/pull/1085) - Disable all deadlines in utils/test_data.py
* [#1090](https://github.com/OasisLMF/OasisLMF/pull/1090) - Request token refresh on HTTP error 403 - Forbidden
* [#1091](https://github.com/OasisLMF/OasisLMF/pull/1091) - Debug complex model execution
* [#1035](https://github.com/OasisLMF/OasisLMF/pull/1092) - No check of parquet output before running model
* [#1093](https://github.com/OasisLMF/OasisLMF/pull/1093) - Fix call to write_summary_levels - missing IL options
* [#1094](https://github.com/OasisLMF/OasisLMF/pull/1094) - Disable GroupID hashing for acceptance tests
* [#1096](https://github.com/OasisLMF/OasisLMF/pull/1096) - Hashing investigation
* [#1097](https://github.com/OasisLMF/OasisLMF/pull/1097) - Fix/pip compile
* [#1099](https://github.com/OasisLMF/OasisLMF/pull/1098) - Implement multiplicative method for total loss computation
* [#1100](https://github.com/OasisLMF/OasisLMF/pull/1100) - OED support for multi-currencies
* [#1101](https://github.com/OasisLMF/OasisLMF/pull/1101) - Always create a correlations.bin, if missing model_settings file is b…
* [#1102](https://github.com/OasisLMF/OasisLMF/pull/1102) - FM documentation update
* [#1107](https://github.com/OasisLMF/OasisLMF/pull/1107) - Fix/678 logger
* [#1110](https://github.com/OasisLMF/OasisLMF/pull/1110) - extent api commands with run-inputs/run-losses options
* [#1108](https://github.com/OasisLMF/OasisLMF/pull/1111) - API client doesn't detect cancelled analysis
* [#1105](https://github.com/OasisLMF/OasisLMF/pull/1112) - Add a 'strict' mode to fail runs if IL/RI is requested but files are missing
* [#1113](https://github.com/OasisLMF/OasisLMF/pull/1113) - Bugfix: out of bounds cdf
* [#906](https://github.com/OasisLMF/OasisLMF/pull/1114) - include "classic" event rates and Metadata in ORD output for oasis outputs
* [#1116](https://github.com/OasisLMF/OasisLMF/pull/1116) - Hide geopandas warning
* [#1119](https://github.com/OasisLMF/OasisLMF/pull/1119) - use correct condpriority to fix cond class exclusion
* [#1120](https://github.com/OasisLMF/OasisLMF/pull/1121) - GUL alloc rule range in MDK has not been updated to reflect addition of rule 3
* [#1129](https://github.com/OasisLMF/OasisLMF/pull/1128) - Add contributing guidelines
* [#1133](https://github.com/OasisLMF/OasisLMF/pull/1133) - Fix/package install error
* [#1135](https://github.com/OasisLMF/OasisLMF/pull/1136) - gulpy appears to hang when sample size is large
* [#1127](https://github.com/OasisLMF/OasisLMF/pull/1137) - Stochastic disaggregation 7 Full Monte Carlo
* [#1139](https://github.com/OasisLMF/OasisLMF/pull/1139) - Hotfix/GitHub actions
* [#1141](https://github.com/OasisLMF/OasisLMF/pull/1140) - `gulpy` produces zero losses for entire items for large number of samples
* [#1144](https://github.com/OasisLMF/OasisLMF/pull/1144) - Release/1.27.0rc3
* [#1132](https://github.com/OasisLMF/OasisLMF/pull/1146) - Make code PEP8 compliant
* [#1148](https://github.com/OasisLMF/OasisLMF/pull/1148) - Remove auto-merge option
* [#1150](https://github.com/OasisLMF/OasisLMF/pull/1149) - Model data in the `runs/lossess-xxx/static` directory are symbolic links
.. _`1.27.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.26.0...1.27.0

`1.27.0rc3`_
 ---------
* [#1120](https://github.com/OasisLMF/OasisLMF/pull/1121) - GUL alloc rule range in MDK has not been updated to reflect addition of rule 3
* [#1129](https://github.com/OasisLMF/OasisLMF/pull/1128) - Add contributing guidelines
* [#1133](https://github.com/OasisLMF/OasisLMF/pull/1133) - Fix/package install error
* [#1135](https://github.com/OasisLMF/OasisLMF/pull/1136) - gulpy appears to hang when sample size is large
* [#1139](https://github.com/OasisLMF/OasisLMF/pull/1139) - Hotfix/GitHub actions
* [#1141](https://github.com/OasisLMF/OasisLMF/pull/1140) - `gulpy` produces zero losses for entire items for large number of samples
* [#1119](https://github.com/OasisLMF/OasisLMF/pull/1119) - use correct condpriority to fix cond class exclusion
.. _`1.27.0rc3`:  https://github.com/OasisLMF/OasisLMF/compare/1.27.0rc1...1.27.0rc3

`1.27.0rc1`_
 ---------
* [#135](https://github.com/OasisLMF/OasisLMF/pull/1024) - Implement OED policy coverage terms in Financial Module
* [#1057](https://github.com/OasisLMF/OasisLMF/pull/1057) - Remove sys.exit(1) calls and replace with exceptions
* [#1058](https://github.com/OasisLMF/OasisLMF/pull/1058) - Correlation map
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1060) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1040](https://github.com/OasisLMF/OasisLMF/pull/1062) - Builtin lookup - missing feedback when all locations are using unsupported LocPerilsCovered
* [#1063](https://github.com/OasisLMF/OasisLMF/pull/1063) - Fix/pre analysis hook
* [#1007](https://github.com/OasisLMF/OasisLMF/pull/1064) - Parquet to csv comparison script
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1065) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1067](https://github.com/OasisLMF/OasisLMF/pull/1067) - Fix/platform run
* [#1068](https://github.com/OasisLMF/OasisLMF/pull/1069) - Implement correlated random number generation in gulpy
* [#1071](https://github.com/OasisLMF/OasisLMF/pull/1071) - Feature/param loading
* [#1072](https://github.com/OasisLMF/OasisLMF/pull/1072) - Update/package requirements
* [#1070](https://github.com/OasisLMF/OasisLMF/pull/1073) - Clean up warning messages
* [#1074](https://github.com/OasisLMF/OasisLMF/pull/1074) - Added lower-case-cols and raise-error flags
* [#1075](https://github.com/OasisLMF/OasisLMF/pull/1075) - setting model_custom_gulcalc disables gulpy
* [#1076](https://github.com/OasisLMF/OasisLMF/pull/1076) - Set ktools to 3.9.2
* [#992](https://github.com/OasisLMF/OasisLMF/pull/1077) - Peril Specific Runs
* [#1049](https://github.com/OasisLMF/OasisLMF/pull/1078) - random number generator can be set to 0 at oasislmf command line
* [#1066](https://github.com/OasisLMF/OasisLMF/pull/1079) - Gulpy failing in distributed runs
* [#1080](https://github.com/OasisLMF/OasisLMF/pull/1080) - add peril_filter to run settings spec
* [#1016](https://github.com/OasisLMF/OasisLMF/pull/1082) - Update package testing
* [#1085](https://github.com/OasisLMF/OasisLMF/pull/1085) - Disable all deadlines in utils/test_data.py
* [#1090](https://github.com/OasisLMF/OasisLMF/pull/1090) - Request token refresh on HTTP error 403 - Forbidden
* [#1091](https://github.com/OasisLMF/OasisLMF/pull/1091) - Debug complex model execution
* [#1035](https://github.com/OasisLMF/OasisLMF/pull/1092) - No check of parquet output before running model
* [#1093](https://github.com/OasisLMF/OasisLMF/pull/1093) - Fix call to write_summary_levels - missing IL options
* [#1094](https://github.com/OasisLMF/OasisLMF/pull/1094) - Disable GroupID hashing for acceptance tests
* [#1096](https://github.com/OasisLMF/OasisLMF/pull/1096) - Hashing investigation
* [#1097](https://github.com/OasisLMF/OasisLMF/pull/1097) - Fix/pip compile
* [#1099](https://github.com/OasisLMF/OasisLMF/pull/1098) - Implement multiplicative method for total loss computation
* [#1100](https://github.com/OasisLMF/OasisLMF/pull/1100) - OED support for multi-currencies
* [#1101](https://github.com/OasisLMF/OasisLMF/pull/1101) - Always create a correlations.bin, if missing model_settings file is b…
* [#1102](https://github.com/OasisLMF/OasisLMF/pull/1102) - FM documentation update
* [#1107](https://github.com/OasisLMF/OasisLMF/pull/1107) - Fix/678 logger
* [#1110](https://github.com/OasisLMF/OasisLMF/pull/1110) - extent api commands with run-inputs/run-losses options
* [#1108](https://github.com/OasisLMF/OasisLMF/pull/1111) - API client doesn't detect cancelled analysis
* [#1105](https://github.com/OasisLMF/OasisLMF/pull/1112) - Add a 'strict' mode to fail runs if IL/RI is requested but files are missing
* [#1113](https://github.com/OasisLMF/OasisLMF/pull/1113) - Bugfix: out of bounds cdf
* [#906](https://github.com/OasisLMF/OasisLMF/pull/1114) - include "classic" event rates and Metadata in ORD output for oasis outputs
* [#1116](https://github.com/OasisLMF/OasisLMF/pull/1116) - Hide geopandas warning
.. _`1.27.0rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.26.3...1.27.0rc1

`1.26.2`_
 ---------
* [#135](https://github.com/OasisLMF/OasisLMF/pull/1024) - Implement OED policy coverage terms in Financial Module
* [#1057](https://github.com/OasisLMF/OasisLMF/pull/1057) - Remove sys.exit(1) calls and replace with exceptions
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1060) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1040](https://github.com/OasisLMF/OasisLMF/pull/1062) - Builtin lookup - missing feedback when all locations are using unsupported LocPerilsCovered
* [#1063](https://github.com/OasisLMF/OasisLMF/pull/1063) - Fix/pre analysis hook
* [#1007](https://github.com/OasisLMF/OasisLMF/pull/1064) - Parquet to csv comparison script
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1065) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1067](https://github.com/OasisLMF/OasisLMF/pull/1067) - Fix/platform run
* [#1071](https://github.com/OasisLMF/OasisLMF/pull/1071) - Feature/param loading
* [#1072](https://github.com/OasisLMF/OasisLMF/pull/1072) - Update/package requirements
* [#1070](https://github.com/OasisLMF/OasisLMF/pull/1073) - Clean up warning messages
* [#1075](https://github.com/OasisLMF/OasisLMF/pull/1075) - setting model_custom_gulcalc disables gulpy
* [#1076](https://github.com/OasisLMF/OasisLMF/pull/1076) - Set ktools to 3.9.2
* [#1048](https://github.com/OasisLMF/OasisLMF/pull/1055) - set modelpy and gulpy as default runtime options
.. _`1.26.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.26.0...1.26.2

`1.26.1`_
 ---------
* [#135](https://github.com/OasisLMF/OasisLMF/pull/1024) - Implement OED policy coverage terms in Financial Module
* [#1057](https://github.com/OasisLMF/OasisLMF/pull/1057) - Remove sys.exit(1) calls and replace with exceptions
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1060) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1040](https://github.com/OasisLMF/OasisLMF/pull/1062) - Builtin lookup - missing feedback when all locations are using unsupported LocPerilsCovered
* [#1063](https://github.com/OasisLMF/OasisLMF/pull/1063) - Fix/pre analysis hook
* [#1007](https://github.com/OasisLMF/OasisLMF/pull/1064) - Parquet to csv comparison script
* [#1059](https://github.com/OasisLMF/OasisLMF/pull/1065) - Missing CSV headers in summarycalc.csv when running chunked losses
* [#1067](https://github.com/OasisLMF/OasisLMF/pull/1067) - Fix/platform run
* [#1071](https://github.com/OasisLMF/OasisLMF/pull/1071) - Feature/param loading
* [#1072](https://github.com/OasisLMF/OasisLMF/pull/1072) - Update/package requirements
* [#1070](https://github.com/OasisLMF/OasisLMF/pull/1073) - Clean up warning messages
* [#1048](https://github.com/OasisLMF/OasisLMF/pull/1055) - set modelpy and gulpy as default runtime options
.. _`1.26.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.26.0...1.26.1

`1.26.0`_
 ---------
* [#1018](https://github.com/OasisLMF/OasisLMF/pull/1026) - Convergence task 11. Set the default number of samples for an analysis from model settings
* [#1029](https://github.com/OasisLMF/OasisLMF/pull/1028) - Class not picked up when using key_server_module_path
* [#1005](https://github.com/OasisLMF/OasisLMF/pull/1030) - in run_ktools use -s flag on kat for ORD elt reports
* [#1031](https://github.com/OasisLMF/OasisLMF/pull/1031) - Feature/group id cleanup
* [#1041](https://github.com/OasisLMF/OasisLMF/pull/1033) - Improve memory usage of gulpy
* [#1034](https://github.com/OasisLMF/OasisLMF/pull/1034) - Distributed Platform Fixes
* [#1036](https://github.com/OasisLMF/OasisLMF/pull/1036) - group id cols updated
* [#1037](https://github.com/OasisLMF/OasisLMF/pull/1037) - use valid buff as look breaker
* [#1038](https://github.com/OasisLMF/OasisLMF/pull/1038) - Fix/parallel chunk script error run errors
* [#1042](https://github.com/OasisLMF/OasisLMF/pull/1042) -  Fixed RI outputs issue in platform-2
* [#1014](https://github.com/OasisLMF/OasisLMF/pull/1043) - gulpy: raise error if `-r` or  `-c` are passed
* [#1046](https://github.com/OasisLMF/OasisLMF/pull/1045) - Memory error while running gulpy on PiWind
* [#1050](https://github.com/OasisLMF/OasisLMF/pull/1050) - Infer the correct mime-type when uploading files to the oasis-platform
* [#1051](https://github.com/OasisLMF/OasisLMF/pull/1053) - Enable output of Average Loss Convergence Table through MDK
* [#1055](https://github.com/OasisLMF/OasisLMF/pull/1055) - Set gulpy and modelpy default run options to True
* [#989](https://github.com/OasisLMF/OasisLMF/pull/989) - adding numba to stitching function
* [#986, #994](https://github.com/OasisLMF/OasisLMF/pull/990) - Feature/986 ods tools dyptes
* [#991](https://github.com/OasisLMF/OasisLMF/pull/991) - Refactor group id seed
* [#996](https://github.com/OasisLMF/OasisLMF/pull/997) - Intermittent bash exit handler failures
* [#999](https://github.com/OasisLMF/OasisLMF/pull/1000) - Port `gulcalc` to Python
* [#1001](https://github.com/OasisLMF/OasisLMF/pull/1002) - Keys Lookup allow parameter to be passed to read_csv in build_merge
* [#1004](https://github.com/OasisLMF/OasisLMF/pull/1004) - Minor Fix: arrange requirements in alphabetical order
* [#1008](https://github.com/OasisLMF/OasisLMF/pull/1008) - Lookup fix if message column is missing
* [#907](https://github.com/OasisLMF/OasisLMF/pull/1009) - generate outputs in chosen ORD technology choice (e.g. parquet)
* [#1010](https://github.com/OasisLMF/OasisLMF/pull/1011) - Support optionally using `gulpy` in the `oasislmf model run` job
* [#1012](https://github.com/OasisLMF/OasisLMF/pull/1012) - Update/readme release section
* [#1013](https://github.com/OasisLMF/OasisLMF/pull/1013) - Feature/gulpy option in cli test
* [#1015](https://github.com/OasisLMF/OasisLMF/pull/1015) - Bugfix: `--random-generator` and `--logging-level` should be parsed as `int` and not as `list` in `gulpy` CLI
* [#1017](https://github.com/OasisLMF/OasisLMF/pull/1017) - Add fix for complex model wrapper calls
.. _`1.26.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.25.1...1.26.0

`1.26.1rc2`_
 ---------
* [#1017](https://github.com/OasisLMF/OasisLMF/pull/1017) - Add fix for complex model wrapper calls
* [#1018](https://github.com/OasisLMF/OasisLMF/pull/1026) - Convergence task 11. Set the default number of samples for an analysis from model settings
* [#1029](https://github.com/OasisLMF/OasisLMF/pull/1028) - Class not picked up when using key_server_module_path
* [#1005](https://github.com/OasisLMF/OasisLMF/pull/1030) - in run_ktools use -s flag on kat for ORD elt reports
.. _`1.26.1rc2`:  https://github.com/OasisLMF/OasisLMF/compare/1.26.1rc1...1.26.1rc2

.. _`1.26.1rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.26.0rc1...1.26.1rc1

`1.26.0rc1`_
 ---------
* [#996](https://github.com/OasisLMF/OasisLMF/pull/997) - Intermittent bash exit handler failures
* [#999](https://github.com/OasisLMF/OasisLMF/pull/1000) - Port `gulcalc` to Python
* [#1001](https://github.com/OasisLMF/OasisLMF/pull/1002) - Keys Lookup allow parameter to be passed to read_csv in build_merge
* [#1004](https://github.com/OasisLMF/OasisLMF/pull/1004) - Minor Fix: arrange requirements in alphabetical order
* [#1008](https://github.com/OasisLMF/OasisLMF/pull/1008) - Lookup fix if message column is missing
* [#907](https://github.com/OasisLMF/OasisLMF/pull/1009) - generate outputs in chosen ORD technology choice (e.g. parquet)
* [#1010](https://github.com/OasisLMF/OasisLMF/pull/1011) - Support optionally using `gulpy` in the `oasislmf model run` job
* [#1012](https://github.com/OasisLMF/OasisLMF/pull/1012) - Update/readme release section
* [#1013](https://github.com/OasisLMF/OasisLMF/pull/1013) - Feature/gulpy option in cli test
* [#1015](https://github.com/OasisLMF/OasisLMF/pull/1015) - Bugfix: `--random-generator` and `--logging-level` should be parsed as `int` and not as `list` in `gulpy` CLI
* [#989](https://github.com/OasisLMF/OasisLMF/pull/989) - adding numba to stitching function
* [#986, #994](https://github.com/OasisLMF/OasisLMF/pull/990) - Feature/986 ods tools dyptes
* [#991](https://github.com/OasisLMF/OasisLMF/pull/991) - Refactor group id seed
.. _`1.26.0rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.25.1...1.26.0rc1

`1.25.1`_
 ---------
* [#987](https://github.com/OasisLMF/OasisLMF/pull/985) - Add a Python implementation of the `cdftocsv` tool
* [#983](https://github.com/OasisLMF/OasisLMF/pull/988) - Unexpected output change in PiWind testing
* [#983](https://github.com/OasisLMF/OasisLMF/pull/982) - Unexpected output change in PiWind testing
.. _`1.25.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.25.0...1.25.1

`1.25.0`_
 ---------
* [#961](https://github.com/OasisLMF/OasisLMF/pull/961) - Feature/docs
* [#973](https://github.com/OasisLMF/OasisLMF/pull/973) - manage -4 and pass through -5 sidx
* [#963](https://github.com/OasisLMF/OasisLMF/pull/974) - Add supported OED versions to model metadata (model_settings.json)
* [#978](https://github.com/OasisLMF/OasisLMF/pull/979) - Model Schema update - replace `numeric_parameters` with `integer_parameters`
* [#980](https://github.com/OasisLMF/OasisLMF/pull/980) - Feature/976 quantile
* [#981](https://github.com/OasisLMF/OasisLMF/pull/981) - Footprint server profiling
.. _`1.25.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.24.1...1.25.0

* [#971](https://github.com/OasisLMF/OasisLMF/pull/972) - Numpy installation issues
.. _`1.24.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.24.0...1.24.1

`1.24.0`_
 ---------
* [#962](https://github.com/OasisLMF/OasisLMF/pull/962) - Prepare 1.23.0 for LTS
* [#950](https://github.com/OasisLMF/OasisLMF/pull/964) - allow event subset to be passed in analysis settings
* [#965](https://github.com/OasisLMF/OasisLMF/pull/965) - Client Fix for update in platform 2.0
* [#966](https://github.com/OasisLMF/OasisLMF/pull/966) - Footprint server
* [#881](https://github.com/OasisLMF/OasisLMF/pull/970) - Enable the use of summary index files by ktools component aalcalc
.. _`1.24.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.23.0...1.24.0

`1.23.0`_
 ---------
* [#762, #915, #838, #839](https://github.com/OasisLMF/OasisLMF/pull/954) - Feature/oed2tests
* [#901](https://github.com/OasisLMF/OasisLMF/pull/900) - fmpy: areaperil_id 8 bytes support
* [#830](https://github.com/OasisLMF/OasisLMF/pull/933) - Step policies: add new calcrule (calcrule 28 + limit)
* [#903](https://github.com/OasisLMF/OasisLMF/pull/903) - Generate Quantile Event Loss Table (QELT) and Quantile Period Loss Table (QPLT)
* [#942](https://github.com/OasisLMF/OasisLMF/pull/943) - Option 'lookup_multiprocessing' not read from config file.
* [#944](https://github.com/OasisLMF/OasisLMF/pull/945) - Loss is not init to 0 for step policy
* [#946](https://github.com/OasisLMF/OasisLMF/pull/946) - Pymodel optimize
* [#948](https://github.com/OasisLMF/OasisLMF/pull/948) - Fix/platform client error
* [#916](https://github.com/OasisLMF/OasisLMF/pull/916) - stashing
* [#953](https://github.com/OasisLMF/OasisLMF/pull/953) - removing memory map attribute
* [#858](https://github.com/OasisLMF/OasisLMF/pull/890) - support parquet for OED
* [#955](https://github.com/OasisLMF/OasisLMF/pull/957) - Update the model references for consistency
* [#959](https://github.com/OasisLMF/OasisLMF/pull/959) - Replace refs to getmodelpy with modelpy
.. _`1.23.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.22.0...1.23.0

`1.22.0`_
 ---------
* [#914](https://github.com/OasisLMF/OasisLMF/pull/929) - numba and numpy version incompatibility
* [#930](https://github.com/OasisLMF/OasisLMF/pull/930) - Fix/update dependencies
* [#857](https://github.com/OasisLMF/OasisLMF/pull/899) - getmodel revamping
* [#901](https://github.com/OasisLMF/OasisLMF/pull/900) - fmpy: areaperil_id 8 bytes support
* [#931](https://github.com/OasisLMF/OasisLMF/pull/931) - Disable memory map for non-utf8 encoding
* [#903](https://github.com/OasisLMF/OasisLMF/pull/903) - Generate Quantile Event Loss Table (QELT) and Quantile Period Loss Table (QPLT)
* [#935](https://github.com/OasisLMF/OasisLMF/pull/935) - fmpy:ignore sidx < -3
* [#936](https://github.com/OasisLMF/OasisLMF/pull/937) - Bash options overriden when running ktools in Subprrocess
* [#913](https://github.com/OasisLMF/OasisLMF/pull/913) - Update API platform client
* [#858](https://github.com/OasisLMF/OasisLMF/pull/890) - support parquet for OED
* [#916](https://github.com/OasisLMF/OasisLMF/pull/916) - stashing
* [#917](https://github.com/OasisLMF/OasisLMF/pull/918) - High memory use in generating dummy model
* [#829](https://github.com/OasisLMF/OasisLMF/pull/919) - Step policies: support files with both step and non-step policies
* [#920](https://github.com/OasisLMF/OasisLMF/pull/921) - conditions for multi-layer accounts file generation
* [#884](https://github.com/OasisLMF/OasisLMF/pull/922) - OasisLMF install fails on OSX Catalina because of ktools installation
* [#739, #740](https://github.com/OasisLMF/OasisLMF/pull/923) - Dummy model occurrence file generation supports repeated events over time and dummy model files are split into static and input directories
* [#924](https://github.com/OasisLMF/OasisLMF/pull/926) - Non UTF-8 portfolio causes model run to crash
.. _`1.22.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.21.0...1.22.0

`1.22.0rc2`_
 ---------
* [#914](https://github.com/OasisLMF/OasisLMF/pull/929) - numba and numpy version incompatibility
* [#930](https://github.com/OasisLMF/OasisLMF/pull/930) - Fix/update dependencies
* [#857](https://github.com/OasisLMF/OasisLMF/pull/899) - getmodel revamping
* [#901](https://github.com/OasisLMF/OasisLMF/pull/900) - fmpy: areaperil_id 8 bytes support
* [#903](https://github.com/OasisLMF/OasisLMF/pull/903) - Generate Quantile Event Loss Table (QELT) and Quantile Period Loss Table (QPLT)
* [#913](https://github.com/OasisLMF/OasisLMF/pull/913) - Update API platform client
* [#858](https://github.com/OasisLMF/OasisLMF/pull/890) - support parquet for OED
* [#916](https://github.com/OasisLMF/OasisLMF/pull/916) - stashing
* [#917](https://github.com/OasisLMF/OasisLMF/pull/918) - High memory use in generating dummy model
* [#829](https://github.com/OasisLMF/OasisLMF/pull/919) - Step policies: support files with both step and non-step policies
* [#920](https://github.com/OasisLMF/OasisLMF/pull/921) - conditions for multi-layer accounts file generation
* [#884](https://github.com/OasisLMF/OasisLMF/pull/922) - OasisLMF install fails on OSX Catalina because of ktools installation
* [#739, #740](https://github.com/OasisLMF/OasisLMF/pull/923) - Dummy model occurrence file generation supports repeated events over time and dummy model files are split into static and input directories
* [#924](https://github.com/OasisLMF/OasisLMF/pull/926) - Non UTF-8 portfolio causes model run to crash
.. _`1.22.0rc2`:  https://github.com/OasisLMF/OasisLMF/compare/1.21.0...1.22.0rc2

`1.21.0`_
 ---------
* [#897](https://github.com/OasisLMF/OasisLMF/pull/897) - added test cases with account terms
* [#803](https://github.com/OasisLMF/OasisLMF/pull/898) - Max Ded back allocation
* [#901](https://github.com/OasisLMF/OasisLMF/pull/900) - fmpy: areaperil_id 8 bytes support
* [#903](https://github.com/OasisLMF/OasisLMF/pull/903) - Generate Quantile Event Loss Table (QELT) and Quantile Period Loss Table (QPLT)
* [#858](https://github.com/OasisLMF/OasisLMF/pull/890) - support parquet for OED
.. _`1.21.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.20.0...1.21.0

`1.21.0rc1`_
 ---------
* [#897](https://github.com/OasisLMF/OasisLMF/pull/897) - added test cases with account terms
* [#803](https://github.com/OasisLMF/OasisLMF/pull/898) - Max Ded back allocation
* [#901](https://github.com/OasisLMF/OasisLMF/pull/900) - fmpy: areaperil_id 8 bytes support
* [#903](https://github.com/OasisLMF/OasisLMF/pull/903) - Generate Quantile Event Loss Table (QELT) and Quantile Period Loss Table (QPLT)
* [#858](https://github.com/OasisLMF/OasisLMF/pull/890) - support parquet for OED
.. _`1.21.0rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.20.0...1.21.0rc1

`1.20.1`_
 ---------
* [#873, #885](https://github.com/OasisLMF/OasisLMF/pull/888) - Feature/873 issues testing update2
* [#857](https://github.com/OasisLMF/OasisLMF/pull/889) - getmodel revamping
* [#892](https://github.com/OasisLMF/OasisLMF/pull/893) - inconsistent assignment of group_id in items file leads to non-repeatable results for the same input
* [#894](https://github.com/OasisLMF/OasisLMF/pull/894) - Fix/arch 2020 update
* [#895](https://github.com/OasisLMF/OasisLMF/pull/895) - Generate Moment Event Loss Table (MELT), Sample Event Loss Table (SELT), Moment Period Loss Table (MPLT) and Sample Period Loss Table (SPLT)
.. _`1.20.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.19.0...1.20.1

`1.20.0`_
 ---------
* [#873, #885](https://github.com/OasisLMF/OasisLMF/pull/888) - Feature/873 issues testing update2
* [#857](https://github.com/OasisLMF/OasisLMF/pull/889) - getmodel revamping
* [#892](https://github.com/OasisLMF/OasisLMF/pull/893) - inconsistent assignment of group_id in items file leads to non-repeatable results for the same input
* [#894](https://github.com/OasisLMF/OasisLMF/pull/894) - Fix/arch 2020 update
* [#895](https://github.com/OasisLMF/OasisLMF/pull/895) - Generate Moment Event Loss Table (MELT), Sample Event Loss Table (SELT), Moment Period Loss Table (MPLT) and Sample Period Loss Table (SPLT)
.. _`1.20.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.19.0...1.20.0

`1.20.0rc1`_
 ---------
* [#873, #885](https://github.com/OasisLMF/OasisLMF/pull/888) - Feature/873 issues testing update2
* [#857](https://github.com/OasisLMF/OasisLMF/pull/889) - getmodel revamping
* [#892](https://github.com/OasisLMF/OasisLMF/pull/893) - inconsistent assignment of group_id in items file leads to non-repeatable results for the same input
* [#894](https://github.com/OasisLMF/OasisLMF/pull/894) - Fix/arch 2020 update
* [#895](https://github.com/OasisLMF/OasisLMF/pull/895) - Generate Moment Event Loss Table (MELT), Sample Event Loss Table (SELT), Moment Period Loss Table (MPLT) and Sample Period Loss Table (SPLT)
.. _`1.20.0rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.19.0...1.20.0rc1

`1.19.0`_
 ---------
* [#856](https://github.com/OasisLMF/OasisLMF/pull/880) - improve memory usage of fmpy
* [#883](https://github.com/OasisLMF/OasisLMF/pull/883) - Fix ri file detection
* [#877](https://github.com/OasisLMF/OasisLMF/pull/877) - Feature/873 automated issues tests
* [#832](https://github.com/OasisLMF/OasisLMF/pull/879) - Consolidate Arch2020 work
.. _`1.19.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.18.0...1.19.0

`1.19.0rc1`_
 ---------
* [#856](https://github.com/OasisLMF/OasisLMF/pull/880) - improve memory usage of fmpy
* [#883](https://github.com/OasisLMF/OasisLMF/pull/883) - Fix ri file detection
* [#877](https://github.com/OasisLMF/OasisLMF/pull/877) - Feature/873 automated issues tests
* [#832](https://github.com/OasisLMF/OasisLMF/pull/879) - Consolidate Arch2020 work
.. _`1.19.0rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.18.0...1.19.0rc1

`1.18.0`_
 ---------
* [#865](https://github.com/OasisLMF/OasisLMF/pull/865) - correction for PolDed6All fields
* [#861](https://github.com/OasisLMF/OasisLMF/pull/866) - Add PALT to genbash
* [#820](https://github.com/OasisLMF/OasisLMF/pull/868) - Pol Fac Contracts
* [#837](https://github.com/OasisLMF/OasisLMF/pull/837) - added new doc
* [#869](https://github.com/OasisLMF/OasisLMF/pull/869) - Feature/761 fm tests
* [#862](https://github.com/OasisLMF/OasisLMF/pull/871) - oasislmf test fm doesn't work and there is no documentation
* [#828](https://github.com/OasisLMF/OasisLMF/pull/872) - RI FM File Generation issue when locations have zero TIV
* [#850](https://github.com/OasisLMF/OasisLMF/pull/870) - Improve exit handler's process cleanup
* [#874](https://github.com/OasisLMF/OasisLMF/pull/875) - Check and set minimum versions for optional packages
* [#846](https://github.com/OasisLMF/OasisLMF/pull/847) - Update package dependencies for flexible lookup code
* [#852](https://github.com/OasisLMF/OasisLMF/pull/854) - Issue with custom lookup_module_path relative path
* [#826](https://github.com/OasisLMF/OasisLMF/pull/826) - Automate Change logs and release notes
* [#860](https://github.com/OasisLMF/OasisLMF/pull/860) - slight interface changes for key server functions
.. _`1.18.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.17.0...1.18.0

`1.17.0`_
 ---------
* [#833](https://github.com/OasisLMF/OasisLMF/pull/834) - Minor issue - error parsing fm CLI help text
* [#831](https://github.com/OasisLMF/OasisLMF/pull/835) - Add timestamps to logger
* [#844](https://github.com/OasisLMF/OasisLMF/pull/836) - Built-in Lookup revamp
* [#840](https://github.com/OasisLMF/OasisLMF/pull/841) - Fix flaky tests in model_preparation/test_lookup.py
* [#843](https://github.com/OasisLMF/OasisLMF/pull/843) - Fix CI pipeline error, double tagging release causes script to fail
* [#842](https://github.com/OasisLMF/OasisLMF/pull/845) - Produce summary index files by default to reduce memory use of ktools output components
* [#816](https://github.com/OasisLMF/OasisLMF/pull/817) - Issue in coverage_type_id grouping of ground up loss results for multi-peril
* [#809](https://github.com/OasisLMF/OasisLMF/pull/818) - Error handling for invalid oasislmf.json config files
* [#849](https://github.com/OasisLMF/OasisLMF/pull/849) - Fix CVE-2021-33503
* [#821](https://github.com/OasisLMF/OasisLMF/pull/821) - Add missing items to data settings
* [#824](https://github.com/OasisLMF/OasisLMF/pull/825) - Inputs directory preparation issue when ORD is enabled
* [#826](https://github.com/OasisLMF/OasisLMF/pull/826) - Automate Change logs and release notes
* [#822](https://github.com/OasisLMF/OasisLMF/pull/827) - Ktools exit handler killing off bash logging on exit
.. _`1.17.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.16.0...1.17.0

`1.17.0rc1`_
 ---------
* [#833](https://github.com/OasisLMF/OasisLMF/pull/834) - Minor issue - error parsing fm CLI help text
* [#831](https://github.com/OasisLMF/OasisLMF/pull/835) - Add timestamps to logger
* [#844](https://github.com/OasisLMF/OasisLMF/pull/836) - Built-in Lookup revamp
* [#840](https://github.com/OasisLMF/OasisLMF/pull/841) - Fix flaky tests in model_preparation/test_lookup.py
* [#843](https://github.com/OasisLMF/OasisLMF/pull/843) - Fix CI pipeline error, double tagging release causes script to fail
* [#842](https://github.com/OasisLMF/OasisLMF/pull/845) - Produce summary index files by default to reduce memory use of ktools output components
* [#816](https://github.com/OasisLMF/OasisLMF/pull/817) - Issue in coverage_type_id grouping of ground up loss results for multi-peril
* [#809](https://github.com/OasisLMF/OasisLMF/pull/818) - Error handling for invalid oasislmf.json config files
* [#821](https://github.com/OasisLMF/OasisLMF/pull/821) - Add missing items to data settings
* [#824](https://github.com/OasisLMF/OasisLMF/pull/825) - Inputs directory preparation issue when ORD is enabled
* [#826](https://github.com/OasisLMF/OasisLMF/pull/826) - Automate Change logs and release notes
* [#822](https://github.com/OasisLMF/OasisLMF/pull/827) - Ktools exit handler killing off bash logging on exit
.. _`1.17.0rc1`:  https://github.com/OasisLMF/OasisLMF/compare/1.16.0...1.17.0rc1

`1.16.0`_
---------
.. start_latest_release
* [#669](https://github.com/OasisLMF/OasisLMF/pull/792) - Revamp of the Key service for improved performance (PR-792)
* [#802](https://github.com/OasisLMF/OasisLMF/pull/802) - Fix for null loss in max deductible case
* [#766](https://github.com/OasisLMF/OasisLMF/issues/766) - Updated FM python documentation
* [#753](https://github.com/OasisLMF/OasisLMF/pull/800) - Added ORD output options for ept/psept and updated json schema
* [#814](https://github.com/OasisLMF/OasisLMF/pull/814) - Fix back allocation child loss loop
* [#815](https://github.com/OasisLMF/OasisLMF/pull/815) - Update requirements and set tests to Python3.8
* [#806](https://github.com/OasisLMF/OasisLMF/issues/806) - Store analysis run settings to outputs via the MDK
* [#807](https://github.com/OasisLMF/OasisLMF/issues/807) - Fixed fmpy numerical errors for step policies producing gross > ground up
.. end_latest_release

`1.15.6`_
---------
* [#803 - Hotfix](https://github.com/OasisLMF/OasisLMF/pull/802) - Partial fix for Max Ded back allocation in fmpy

`1.15.5`_
---------
* [#798 - Hotfix](https://github.com/OasisLMF/OasisLMF/issues/798) - Fix process cleanup on ktools script exit
* [#799 - Hotfix](https://github.com/OasisLMF/OasisLMF/issues/799) - Fix fmpy, multilayer stream writer for RI
* [#794 - Hotfix](https://github.com/OasisLMF/OasisLMF/issues/794) - Fix column duplication when using "tiv, loc_id, coverage_type_id" in oed_field

`1.15.4`_
---------
* [#464 - Hotfix](https://github.com/OasisLMF/OasisPlatform/issues/464) - Worker stuck idle on some bash errors
* [#785 - Hotfix](https://github.com/OasisLMF/OasisLMF/issues/785) - fmsummaryxref.csv not copied into top level RI directory

`1.15.3`_
---------
* [#780](https://github.com/OasisLMF/OasisLMF/pull/780) - Fix for fmpy, last event missing when using event terminator 0,0

`1.15.2`_
---------
* [#777](https://github.com/OasisLMF/OasisLMF/issues/777) - Summarise ground up only runs using Insured loss fields
* [#776](https://github.com/OasisLMF/OasisLMF/pull/776) - Fix tiv summary info feature, Pandas compatibility & column select issue

`1.15.1`_
---------
* [#771 - Hotfix](https://github.com/OasisLMF/OasisLMF/issues/771) - Fix running GUL only analyses with fmpy

`1.15.0`_
---------
* [#765](https://github.com/OasisLMF/OasisLMF/pull/765) - Add a first pass of FM python documentation
* [#770](https://github.com/OasisLMF/OasisLMF/pull/770) - Fix issue in lookup factory no results check
* [#755](https://github.com/OasisLMF/OasisLMF/pull/755) - Added updates fixes to fm testing tool
* [#759](https://github.com/OasisLMF/OasisLMF/issues/759) - Switched fmpy to the default financial module
* [#688](https://github.com/OasisLMF/OasisLMF/issues/688) - Added TIV reporting to summary info files
* [#623](https://github.com/OasisLMF/OasisLMF/issues/623) - Added check to raise an error if a locations file references account numbers missing from the account file.
* [#749](https://github.com/OasisLMF/OasisLMF/pull/749) - The Group ids can now be set by the following internal oasis fields 'item_id', 'peril_id', 'coverage_id', and 'coverage_type_id'
* [#760](https://github.com/OasisLMF/OasisLMF/pull/760) - Upgraded test harness for financial module and added numerical tests for fmpy.
* [#754](https://github.com/OasisLMF/OasisLMF/issues/754) - Added validation for unsupported special conditions
* [#752](https://github.com/OasisLMF/OasisLMF/issues/752) - Fixed issue with fmpy - not calculating net loss across all layers correctly.
* [#751](https://github.com/OasisLMF/OasisLMF/issues/751) - Remove dependence on ReinsNumber order when assigning layer ID
* [#763](https://github.com/OasisLMF/OasisLMF/issues/763) - Dropped binary wheel package for Mac OSX
* [#750](https://github.com/OasisLMF/OasisLMF/issues/750) - Switched oasislmf `exposure run` to use gul stream type 2 by default
* [#391](https://github.com/OasisLMF/OasisLMF/issues/391) - Added fix so error is raise when no data is returned from keys server.

`1.14.0`_
---------
* [#724](https://github.com/OasisLMF/OasisLMF/issues/724) - fm file generation issues with fac when combined with other types of reinsurance
* [#735](https://github.com/OasisLMF/OasisLMF/pull/735) - Bug fixes for python FM module
* [#731](https://github.com/OasisLMF/OasisLMF/issues/731) - Fix health check on exposure summary unittest
* [#692](https://github.com/OasisLMF/OasisLMF/issues/692) - Added FM testing jupyter notebook [binder link](https://mybinder.org/v2/gh/OasisLMF/OasisLMF/develop?filepath=FmTesting.ipynb)
* [#658](https://github.com/OasisLMF/OasisLMF/issues/658) - Changes in input file generation to extend special conditions functionality (requires testing)
* [#738](https://github.com/OasisLMF/OasisLMF/pull/738) - Fix setup.py fallback for ktools install in development mode
* [#665](https://github.com/OasisLMF/OasisLMF/issues/665) - Provide CL arguments for generating dummy model files
* [#744](https://github.com/OasisLMF/OasisLMF/pull/744) - Compatibility fix for older pandas versions
* [#708](https://github.com/OasisLMF/OasisLMF/issues/708) - Check for case sensitive event/occ sets with a fallback to lowercase names
* [#737](https://github.com/OasisLMF/OasisLMF/issues/737) - Added flag `--ktools-event-shuffle` to support ktools feature [Issue 119](https://github.com/OasisLMF/ktools/issues/119)

`1.13.2`_
---------
* [#690](https://github.com/OasisLMF/OasisLMF/pull/690) - Raise error is output node is missing its output_id
* [#700](https://github.com/OasisLMF/OasisLMF/issues/700) - Update error guard to cover all ktools binaries
* [#701](https://github.com/OasisLMF/OasisLMF/issues/701) - Fixed api search crash when metadata is empty
* [#702](https://github.com/OasisLMF/OasisLMF/issues/702) - Fixed error When Input data contains commas
* [#705](https://github.com/OasisLMF/OasisLMF/issues/705) - Select keys generator based on class type
* [#710](https://github.com/OasisLMF/OasisLMF/issues/710) - Added missing layer calcrules for limit only
* [#712](https://github.com/OasisLMF/OasisLMF/issues/712) - Fix missing gul_errors_map.csv file
* [#713](https://github.com/OasisLMF/OasisLMF/issues/713) - Fix for gul_errors_map containing duplicate columns
* [#722](https://github.com/OasisLMF/OasisLMF/issues/722) - Fixed error creating summary levels in Pandas 1.2.0

`1.13.1`_
---------
* [#709](https://github.com/OasisLMF/OasisLMF/issues/709) - Fix issue with generation of profile IDs for step policies that include separate coverages

`1.13.0`_
---------
* [#694](https://github.com/OasisLMF/OasisLMF/pull/694) - Schema update, restrict output options by eventset
* [#670](https://github.com/OasisLMF/OasisLMF/issues/670) - Add CLI flags for lookup multiprocessing options
* [#695](https://github.com/OasisLMF/OasisLMF/issues/695) - Set default value of optional OED step policy fields to 0
* [#686](https://github.com/OasisLMF/OasisLMF/issues/686) - Fixed fmpy numerical issues when using allocrule 1
* [#681](https://github.com/OasisLMF/OasisLMF/issues/681) - Added fmpy support for stepped policies
* [#680](https://github.com/OasisLMF/OasisLMF/issues/680) - Added user defined return periods option to `analysis_settings.json`
* [#677](https://github.com/OasisLMF/OasisLMF/pull/677) - Enabled Fmpy to handle multiple input streams
* [#678](https://github.com/OasisLMF/OasisLMF/issues/678) - Fixed environment variable loading

`1.12.1`_
---------
* [#674](https://github.com/OasisLMF/OasisLMF/pull/674) - Introduce check for step policies in genbash

`1.12.0`_
---------
* [#413](https://github.com/OasisLMF/OasisLMF/issues/413) - Peril Handling in Input Generation
* [#661](https://github.com/OasisLMF/OasisLMF/issues/661) - Added experimental financial module written in Python 'fmpy'
* [#662](https://github.com/OasisLMF/OasisLMF/issues/662) - Define relationships between event and occurrence in model_settings
* [#671](https://github.com/OasisLMF/OasisLMF/issues/671) - Fix issue with loading booleans in oasislmf.json and corrected the 'ktools-fifo-relative' flag
* [#666](https://github.com/OasisLMF/OasisLMF/pull/666) - Fix files created to generate-oasis-files, being cleared

`1.11.1`_
---------
* [#653](https://github.com/OasisLMF/OasisLMF/issues/653) - Fix pre-analysis exposure modification for generate-oasis-files command

`1.11.0`_
---------
* [#598](https://github.com/OasisLMF/OasisLMF/issues/598) - Fac Contracts being applied as multiple layers in RI file generation
* [#648](https://github.com/OasisLMF/OasisLMF/issues/648) - Correlation Group OED field to drive group_id directly
* [#458](https://github.com/OasisLMF/OasisLMF/issues/458) - Keys lookup response clean up
* [#575](https://github.com/OasisLMF/OasisLMF/issues/575) - Add option to test multi-peril in oasislmf exposure run and oasislmf test fm
* [#606](https://github.com/OasisLMF/OasisLMF/issues/606) - missing combination of terms in calcrules to add - part 2
* [#568](https://github.com/OasisLMF/OasisLMF/issues/568) - Min/max deductible not working when prior level locations are partially limited in OED input
* [#640](https://github.com/OasisLMF/OasisLMF/issues/640) - Use categorical dtype to reduce the memory usage of files generation
* [PR 651](https://github.com/OasisLMF/OasisLMF/pull/651) - Fixing typo in Probabilistic and usage of historical vs historic
* [PR 654](https://github.com/OasisLMF/OasisLMF/pull/654) - add check if epa when copying file for file generation
* [PR 652](https://github.com/OasisLMF/OasisLMF/pull/652) - If a path parameter is an empty string, load default value
* [PR 660](https://github.com/OasisLMF/OasisLMF/pull/660) - Fix pre Analysis input file paths for `oasislmf model run`

`1.10.2`_
---------
* [8fdc512](https://github.com/OasisLMF/OasisLMF/pull/644) - Fix issue with introduction of erroneous duplicate rows when calculating aggregated TIVs

`1.10.1`_
---------
* Fix issue with supplier model runner

`1.10.0`_
---------
* [#573](https://github.com/OasisLMF/OasisLMF/issues/573) - Extract and apply default values for OED mapped FM terms
* [#581](https://github.com/OasisLMF/OasisLMF/issues/581) - Split calc. rules files
* [#604](https://github.com/OasisLMF/OasisLMF/issues/604) - Include unsupported coverages in type 2 financial terms calculation
* [#608](https://github.com/OasisLMF/OasisLMF/issues/608) - Integration of GUL-FM load balancer
* [#614](https://github.com/OasisLMF/OasisLMF/issues/614) - Refactor oasislmf package
* [#617](https://github.com/OasisLMF/OasisLMF/issues/617) - Fix TypeError in write_exposure_summary
* [#636](https://github.com/OasisLMF/OasisLMF/issues/636) - Improve error handling in run_ktools.sh
* Fix minor issues in oasis file generation and complex model runs

`1.9.1`_
--------
* [#630](https://github.com/OasisLMF/OasisLMF/issues/630) - full_correlation gulcalc option creates large output files.

`1.9.0`_
--------
* [#566](https://github.com/OasisLMF/OasisLMF/issues/566) - Handle unlimited LayerLimit without large default value
* [#574](https://github.com/OasisLMF/OasisLMF/issues/574) - Use LayerNumber to identify unique policy layers in gross fm file generation
* [#578](https://github.com/OasisLMF/OasisLMF/issues/578) - Added missing combination of terms in calcrules
* [#603](https://github.com/OasisLMF/OasisLMF/issues/603) - Add type 2 financial terms tests for multi-peril to regression test
* [PR 600](https://github.com/OasisLMF/OasisLMF/pull/600) - Added Scripts for generated example model data for testing.

`1.8.3`_
--------
* [#601](https://github.com/OasisLMF/OasisLMF/issues/601) - Fix calculations for type 2 deductibles and limits in multi-peril models

`1.8.2`_
--------
* [#599](https://github.com/OasisLMF/OasisLMF/issues/599) - Allow setting 'loc_id' externally
* [#594](https://github.com/OasisLMF/OasisLMF/issues/594) - Pass copy of location df to custom lookup to avoid side effects
* [#593](https://github.com/OasisLMF/OasisLMF/issues/593) - Fail fast on analysis settings formatting problem
* [#591](https://github.com/OasisLMF/OasisLMF/issues/591) - Update pinned pandas package
* [#588](https://github.com/OasisLMF/OasisLMF/issues/588) - AreaCode is defined as "string" in OED, but loaded as a number in the DF
* [#596](https://github.com/OasisLMF/OasisLMF/issues/596) - Incorrect number of locations in Overview
* [3dce18f](https://github.com/OasisLMF/OasisLMF/pull/595/commits/3dce18f5872c2855f29548845212bdde8813f472) - Relax required fields in analysis_settings validation
* [bd052a6](https://github.com/OasisLMF/OasisLMF/pull/595/commits/bd052a641b53db5284fb9609b43d6080df77711c) - Fix issue in gen bash, only enable an output type if summary section exists

`1.8.1`_
--------
* [#589](https://github.com/OasisLMF/OasisLMF/issues/589) - Schema fix to allow for 0 samples
* [#583](https://github.com/OasisLMF/OasisLMF/pull/583) - Reduce memory use in gul_inputs creation (DanielFEvans)
* [#582](https://github.com/OasisLMF/OasisLMF/issues/582) -  Check for calc_type in all sections

`1.8.0`_
--------
* [#579](https://github.com/OasisLMF/OasisLMF/issues/579) - Install complex_itemstobin and complex_itemstocsv
* [#565](https://github.com/OasisLMF/OasisLMF/issues/565) - Non-unicode CSV data is not handled neatly
* [#570](https://github.com/OasisLMF/OasisLMF/issues/570) - Issue with item_id to from_agg_id mapping at level 1
* [#556](https://github.com/OasisLMF/OasisLMF/issues/556) - review calc_rules.csv mapping for duplicates and logical gaps
* [#549](https://github.com/OasisLMF/OasisLMF/issues/549) - Add FM Tests May 2020
* [#555](https://github.com/OasisLMF/OasisLMF/issues/555) - Add JSON schema validation on CLI
* [#577](https://github.com/OasisLMF/OasisLMF/issues/577) - Add api client progressbars for OasisAtScale


`1.7.1`_
--------
* #553 - Fix alc rule mapping error
* #550 - Fix enbash fmcalc and full_correlation
* #548 - Fix UL Alloc Rule 0
* Fix - Assign loc_id by sorted values of (LocNum, AccNum, PortNum) - location file resistant to reordering rows
* Fix - default `run_dir` in `oasislmf model generate-exposure-pre-analysis` cmd

`1.7.0`_
--------
* #497 - Add exception wrapping to OasisException
* #528 - FM validation tests with % damage range
* #531 - item file ordering of item_id
* #533 - Added new FM acceptance tests
* Added - Pre-analysis exposure modification (CLI interface)
* Added - revamped CLI Structure

`1.6.0`_
--------
* Fix #513 - Breaking change in msgpack 1.0.0
* Fix #503 - Change areaperil id datatype to unit64
* Fix #481 - Corrections to fm_profile for type 2 terms
* Fix #512 - Issue in generate rtree index CLI
* Fix #516 - Refactored the `upload_settings` method in API client
* Fix #514 - fix ; issues in LocPerilsCovered
* Fix #515 - Store the `loc_id` of failed location rows
* Added #508 - fm12 acceptance test
* Added #480 - Extend calcrules to cover more combinations of financial terms
* Added #523 - Long description field to `model_settings.json` schema
* Added #524 - Total TIV sums in exposure report
* Added #527 - Group OED fields from model settings
* Added #506 - Improve performance in `write_exposure_summary()`

`1.5.1`_
--------
* Fix - Issue in IL file generation, `fm_programme` file missing agg_id rows

`1.5.0`_
--------

* Added step policy support
* Added #453 - Allow user to select group_id based on columns in loc file
* Added #474 - Option to set gulcalc command - raises an error if not in path
* Update to Model Settings schema, #478 #484 #485
* Update #464 - API client with new Queued Job states
* Update #470 - Model_settings.json schema
* Fix #491 -  in `oasislmf exposure run` command
* Fix #477 - setup.py fails when behind a proxy
* Fix #482 - symlink error when rerunning analysis using existing analysis_folder
* Fix #460 - CLI, remove use of lowercase '-c'
* Fix #493 - generate_model_losses fix for spaces in filepath
* Fix #475 - Prevent copy of model_data directory on OSError
* Fix #486 - Run error using `pandas==1.0.0`
* Fix #459 - File generation issue in fm_programme
* Fix #456 - Remove calls to `get_ids` in favour of pandas groupby
* Fix #492 - ComplexModel error guard run in subshell
* Fix #451 - ComplexModel error guard in bash script
* Fix #415 - RI String matching issue
* Fix #462 - Issue in fm_programmes file generation
* Fix #463 - Incorrect limits in FM file generation
* Fix #468 - Fifo issue in Bash script generation


`1.4.6`_
--------
* Update to model_settings schema
* Fixes #452 - Check columns before grouping output
* Fixes #451 - Error checking ktools runs for complex models

`1.4.5`_
--------
* Fix for fm_programme mapping
* Fix for IL files generation
* Fix issue #439 - il summary groups
* Reduce memory use in GUL inputs generation (#440)
* Fix for api client - handle rotating refresh token
* Feature/setting schemas (#438)
* Update API client - add settings JSON endpoints (#444)
* Add fully correlated option to MDK (#446)
* Add dtype conversion and check for valid OED peril codes (#448)

`1.4.4`_
--------
* Hotfix - Added the run flag `--ktools-disable-guard` option for complex models & custom binaries

`1.4.3`_
--------
* Added support for compressed file extensions
* Fix docker kill error
* Fix in IL inputs
* Fix for multiprocessing lookup
* Fix for summary info data types
* Set IL alloc rule default to 3
* Various fixes for CLI
* Various fixes for ktools scripts

`1.4.2`_
--------
* Added Multi-process keys lookup
* Updated API client
* Added Verifying model files command
* Updated command line flags with backwards compatibility

`1.4.1`_
--------
* Added bash autocomplete #386
* Fix for exposure data types on lookup #387
* Fix for non-OED fields in summary levels #377
* Fix in Reinsurance Layer Logic #381
* Refactor deterministic loss generation #371
* Added bdist package for OSX #372
* Added Allocation rule for Ground up loss #376

`1.4.0`_
--------
* Cookiecutter CLI integration - commands for creating simple and complex Oasis model projects/repositories from project templates
* Extend calc. rules and FM test coverage
* Various fixes in FM and data utils
* Various fixes and updates for the API client module
* Add ktools static binary bdist_wheel to published package
* Fix for Layer_id in file generation
* Performance improvment and fixes for the exposure summary reporting
* Added optional `--summarise-exposure` flag for exposure report output
* Added `exposure_summary_levels.json` file to inputs directory, lists valid OED columns to build summary groups
* Added summary info files to output directory `gul_S1_summary-info.csv` which lists data for grouping summary_ids
* Ktools updated to v3.1.0

`1.3.10`_
---------
* Hotfix release - fix for models using custom lookups

`1.3.9`_
--------
* Updated validation and fixes for FM file generation
* Fixes for exposure-summary reporting
* Fixes for FM calc rule selection

`1.3.8`_
--------
* Add FM support for processing types and codes for deductibles and limits
* Improvements for complex model support and logging
* Update to summary sets for grouping results
* Exposure reporting added
* Fixes for Oasis files generation
* Updates to RI and Acceptance testing
* new sub-command `oasislmf exposure ..` for running and validating deterministic models

`1.3.7`_
--------
* Hotfix - ktools-num-processes not read as int from CLI

`1.3.6`_
--------
* Hotfix - Custom lookup issue in manager

`1.3.5`_
--------
* Issue found in ktools `3.0.7` hotfix downgrade to `3.0.6`

`1.3.4`_
--------
* Optimise FM/IL component (IL input items + input files generation)
* Optimise Oasis files generation (GUL + IL input items + input files generation)
* Upgrade data-related utilities
* Update API client
* Fixes for windows compatibility
* Support for Python 2.7 Ends

`1.3.3`_
--------
* Hotfix for GUL files generation
* Hotfix for lookup index generation
* Hotfix for ktools bash script

`1.3.2`_
--------
* Hotfix fix for analysis_settings custom model worker
* Hotfix tweak for deterministic RI loss calculation

`1.3.1`_
--------
* Hotfix for path issue with the analysis_setttings file
* Downgraded ktools from `3.0.6` to `3.0.5` fix pending in fmcalc

`1.3.0`_
--------
* Remove CSV file transformations from Oasis files generation - use OED source exposure directly
* Integrate backend RI functionality with the CLI model subcommands - full RI losses can now be generated
* Add new CLI subcommand for deterministic loss generation including direct and RI losses
* Optimise FM component (13x speedup achieved)
* Add support for custom complex models, python version of ground up losses `gulcalc.py`

`1.2.8`_
--------
* Hotfix for Ktools, version is now 3.0.5
* Hotfix for API Client Upload timeout issue

`1.2.7`_
--------
* Hotfix in Generate-Losses command

`1.2.6`_
--------
* Added Reinsurance to CLI
* Added Ktools run options to CLI
* Fix for Ktools Memory limits in Genbash

`1.2.5`_
--------
* Fix for setting Alloc Rule in genbash

`1.2.4`_
--------
* Fix for Windows 10 (Linux Sub-system), FIFO queues moved into `/tmp/<random>`
* Fix for Reinsurance, Set RiskLevel = `SEL` as default when value is not set
* Fix, calc rule for all positivedeductibles
* Fixes for new API Client
* Added Deterministic loss generation
* Added FM acceptance tests
* Added Automated testing

`1.2.3`_
--------
* Hotfix for Reinsurance required fields
* Dockerfile and run script for unittests

`1.2.2`_
--------
* Added API client for OED API update
* New MDK commands to run the updated API client
* Improved FM file generation testing
* Fixes to scope filters to correctly handle account, policy and location combinations.
* Added portfolio and location group scope filters.
* Fixes to required fields and default values to match OED
* Fixed binary file writing bug, corrupted tar output files


`1.2.1`_
--------

* Compatibility fix for new API worker
* Fix for Parsing config.json on MDK command line
* Fix for Reinsurance
* Add Reinsurance tests
* Fix GUL item group IDs to index item loc. IDs

`1.2.0`_
--------

* Update concurrency utils - replace multiprocessing.Pool by billiard.Pool in multiprocessing wrapper (oasislmf.utils.concurrency.multiprocess) to fix a problem with Celery tasks unable to run applications which use processes or process pools created using the built-in multiprocessing package (https://github.com/celery/celery/issues/1709)
* Add IL/FM support
* Various optimisations, including to GUL items generation

`1.1.27`_ (beta)
----------------

* Fix for installing ktools on mac OSX (3.0.1)
* Fix for Reinsurance input file validation
* Update Subcommand `oasislmf model generate-oasis-file` to use optional xml validation
* Update for unittest stability on CI/CD

`1.1.26`_ (beta)
----------------

* Merge in reinsurance update from feature/reinsurance
* Fix ktools install using pip instal editable mode `pip install -e ..`

`1.1.25`_ (beta)
----------------

* Fix install issue with utils/keys_data.py - file removed as its no longer used.

`1.1.24`_ (beta)
----------------

* Fix ordering of bulk lookup generation in base generic lookup - records should be generated as (loc. ID, peril ID, coverage type ID) combinations.

`1.1.23`_ (beta)
----------------

* Performace update for exposure transforms `transform-source-to-canonical` and `transform-canonical-to-model`.
* Validation of transform is now optional `--xsd-validation-file-path`, if no value is given this step is skipped.

`1.1.22`_ (beta)
----------------

* Fix bug in coverage type matching of canonical items and keys items in the GUL items generator in the exposure manager

`1.1.21`_ (beta)
----------------

* Enable lookup framework and exposure manager to support multi-peril and multi-coverage type models

`1.1.20`_ (beta)
----------------

* Refactor lookup factory to be compatible with new lookup framework
* Various enhancements to the peril areas index class, file index generation command and peril utils
* Fix for installing pip package without building ktools if binaries exist in system path.

`1.1.19`_ (beta)
----------------

* Fix string lowercasing of lookup config values in new lookup classes
* Fix object pickling to account for Python major version when creating Rtree file index from areas file
* Various fixes to arg parsing and logging in Rtree file index model subcommand class

`1.1.18`_ (beta)
----------------

* Upgrade peril utils, including a custom Rtree index class for peril areas
* Implement MDK model subcommand for writing Rtree file indexes for peril areas from peril area (area peril) files
* Various fixes to the new lookup class framework


`1.1.17`_ (beta)
----------------

* Fix list sorting in exposure manager to use explicit sort key

`1.1.15`_ (beta)
----------------

* Add new lookup class framework in `keys` subpackage

`1.1.14`_ (beta)
----------------

* Add MDK model subcommands for performing source -> canonical and canonical -> model file transformations
* Python 3 compatibility fixes to replace map and filter statements everywhere by list comprehensions

`1.1.13`_ (beta)
----------------

* Add performance improvement for exposure transforms
* Limit exposure validation messages to log level `DEBUG`

`1.1.12`_ (beta)
----------------

* Add concurrency utils (threading + multiprocessing) to `utils` sub. pkg.

`1.1.11`_ (beta)
----------------

* Hotfix for get_analysis_status - fixes issue in client api

`1.1.10`_ (beta)
----------------

* Hotfix for utils INI file loading method - fix parsing of IP
  strings

`1.0.9`_ (beta)
---------------

* Hotfix for JSON keys file writer in keys lookup factory - convert
  JSON string to Unicode literal before writing to file

`1.0.8`_ (beta)
---------------

* Enable custom model execution parameters when running models

`1.0.6`_ (beta)
---------------

* Remove timestamped Oasis files from Oasis files generation pipeline

`1.0.5`_ (beta)
---------------

* Add keys error file generation method to keys lookup factory and make
  exposures manager generate keys error files by default

`1.0.1`_ (beta)
---------------

* Add console logging

.. _`1.16.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.6...1.16.0
.. _`1.15.6`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.5...1.15.6
.. _`1.15.5`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.4...1.15.5
.. _`1.15.4`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.3...1.15.4
.. _`1.15.3`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.2...1.15.3
.. _`1.15.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.1...1.15.2
.. _`1.15.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.15.0...1.15.1
.. _`1.15.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.14.0...1.15.0
.. _`1.14.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.13.2...1.14.0
.. _`1.13.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.13.1...1.13.2
.. _`1.13.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.13.0...1.13.1
.. _`1.13.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.12.1...1.13.0
.. _`1.12.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.12.0...1.12.1
.. _`1.12.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.11.1...1.12.0
.. _`1.11.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.11.0...1.11.1
.. _`1.11.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.10.2...1.11.0
.. _`1.10.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.10.1...1.10.2
.. _`1.10.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.10.0...1.10.1
.. _`1.10.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.9.1...1.10.0
.. _`1.9.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.9.0...1.9.1
.. _`1.9.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.8.3...1.9.0
.. _`1.8.3`:  https://github.com/OasisLMF/OasisLMF/compare/1.8.2...1.8.3
.. _`1.8.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.8.1...1.8.2
.. _`1.8.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.8.0...1.8.1
.. _`1.8.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.7.1...1.8.0
.. _`1.7.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.7.0...1.7.1
.. _`1.7.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.6.0...1.7.0
.. _`1.6.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.5.1...1.6.0
.. _`1.5.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.5.0...1.5.1
.. _`1.5.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.6...1.5.0
.. _`1.4.6`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.5...1.4.6
.. _`1.4.5`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.4...1.4.5
.. _`1.4.4`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.3...1.4.4
.. _`1.4.3`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.2...1.4.3
.. _`1.4.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.1...1.4.2
.. _`1.4.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.4.0...1.4.1
.. _`1.4.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.10...1.4.0
.. _`1.3.10`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.9...1.3.10
.. _`1.3.9`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.8...1.3.9
.. _`1.3.8`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.7...1.3.8
.. _`1.3.7`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.6...1.3.7
.. _`1.3.6`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.5...1.3.6
.. _`1.3.5`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.4...1.3.5
.. _`1.3.4`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.3...1.3.4
.. _`1.3.3`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.2...1.3.3
.. _`1.3.2`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.1...1.3.2
.. _`1.3.1`:  https://github.com/OasisLMF/OasisLMF/compare/1.3.0...1.3.1
.. _`1.3.0`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.8...1.3.0
.. _`1.2.8`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.7...1.2.8
.. _`1.2.7`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.6...1.2.7
.. _`1.2.6`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.5...1.2.6
.. _`1.2.5`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.4...1.2.5
.. _`1.2.4`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.3...1.2.4
.. _`1.2.3`:  https://github.com/OasisLMF/OasisLMF/compare/1.2.2...1.2.3
.. _`1.2.2`:  https://github.com/OasisLMF/OasisLMF/compare/d6dbf25...master
.. _`1.2.1`:  https://github.com/OasisLMF/OasisLMF/compare/f4d7390...master
.. _`1.2.0`:  https://github.com/OasisLMF/OasisLMF/compare/ad91e2a...master
.. _`1.1.27`: https://github.com/OasisLMF/OasisLMF/compare/ac4375e...master
.. _`1.1.26`: https://github.com/OasisLMF/OasisLMF/compare/dac703e...master
.. _`1.1.25`: https://github.com/OasisLMF/OasisLMF/compare/3a4b983...master
.. _`1.1.24`: https://github.com/OasisLMF/OasisLMF/compare/8f94cab...master
.. _`1.1.23`: https://github.com/OasisLMF/OasisLMF/compare/0577497...master
.. _`1.1.22`: https://github.com/OasisLMF/OasisLMF/compare/bfeee86...master
.. _`1.1.21`: https://github.com/OasisLMF/OasisLMF/compare/c04dc73...master
.. _`1.1.20`: https://github.com/OasisLMF/OasisLMF/compare/fd31879...master
.. _`1.1.19`: https://github.com/OasisLMF/OasisLMF/compare/5421b91...master
.. _`1.1.18`: https://github.com/OasisLMF/OasisLMF/compare/da8fcba...master
.. _`1.1.17`: https://github.com/OasisLMF/OasisLMF/compare/de90f11...master
.. _`1.1.15`: https://github.com/OasisLMF/OasisLMF/compare/18b34b9...master
.. _`1.1.14`: https://github.com/OasisLMF/OasisLMF/compare/f3e0ee8...master
.. _`1.1.13`: https://github.com/OasisLMF/OasisLMF/compare/33f96fd...master
.. _`1.1.12`: https://github.com/OasisLMF/OasisLMF/compare/5045ca2...master
.. _`1.1.10`: https://github.com/OasisLMF/OasisLMF/compare/a969192...master
.. _`1.0.9`:  https://github.com/OasisLMF/OasisLMF/compare/17c691b...master
.. _`1.0.8`:  https://github.com/OasisLMF/OasisLMF/compare/8eeaeaf...master
.. _`1.0.6`:  https://github.com/OasisLMF/OasisLMF/compare/9578398...master
.. _`1.0.5`:  https://github.com/OasisLMF/OasisLMF/compare/c87c782...master
.. _`1.0.1`:  https://github.com/OasisLMF/OasisLMF/compare/7de227d...master
