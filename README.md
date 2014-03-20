Quantum Chemistry Speed Test
============================

**The rules**: Calculations must only use a single core. The B3LYP used should be that used by default by Gaussian and NWChem (namely the VWN3 not VWN5). And please, no Gaussian input files or results.

Various people have submitted results:
- [Eric Berquist](http://github.com/berky/qmspeedtest)
- [Karol Langner](http://github.com/langner/qmspeedtest)
- [Michael Banck](http://github.com/mbanck/qmspeedtest)
- [Noel O'Boyle](http://github.com/baoilleach/qmspeedtest)
- [Pedro Silva](http://github.com/PedroJSilva/qmspeedtest)

Please fork the [original repo](http://github.com/baoilleach/qmspeedtest) and submit your own!

Eric Berquist's results
----------------------

**Machine:** AMD Opteron(tm) Processor 6172 [Magny Cours] @ 2.10 GHz running 64-bit RHEL 6

**Fancy compiler or maths libraries used when compiling:** Intel compilers w/ MKL (various versions)

### HF
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th>
<th>Steps</th>
<th>per step</th>
<th>Total E</th>
<th>HOMO</th>
<th>LUMO</th>
</tr>
<tr>
<td>DALTON</td><td>2013.2</td>
<td>26.8</td>
<td>19</td>
<td>1.41</td>
<td>-644.675706212821</td>
<td>-0.35364477</td>
<td>0.07433447</td>
</tr>
<tr>
<td>GAMESS</td><td>2013-05-01</td>
<td>10.8</td>
<td>30</td>
<td>0.36</td>
<td>-644.6757056212</td>
<td>-0.3536</td>
<td>0.0744</td>
</tr>
<tr>
<td>NWChem</td><td>6.1.1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ORCA</td><td>2.9.1</td>
<td>28.6</td>
<td>13</td>
<td>2.20</td>
<td>-644.675706036271</td>
<td>-0.353622</td>
<td>0.074344</td>
</tr>
<tr>
<td>ORCA</td><td>3.0.1</td>
<td>11</td>
<td>12</td>
<td>0.9</td>
<td>-644.675706036270</td>
<td>-0.353622</td>
<td>0.074344</td>
</tr>
<tr>
<td>Q-Chem</td><td>4.1.0.1</td>
<td>6.1</td>
<td>14</td>
<td>0.43</td>
<td>-644.675706161474</td>
<td>-0.354</td>
<td>0.074</td>
</tr>
<tr>
<td>TURBOMOLE</td><td>6.5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th>
<th>Steps</th>
<th>per step</th>
<th>Total E</th>
<th>HOMO</th>
<th>LUMO</th>
</tr>
<tr>
<td>DALTON</td><td>2013.2</td>
<td>26.8</td>
<td>19</td>
<td>1.41</td>
<td>-644.675706212821</td>
<td>-0.35364477</td>
<td>0.07433447</td>
</tr>
<tr>
<td>GAMESS</td><td>2013-05-01</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>NWChem</td><td>6.1.1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ORCA</td><td>2.9.1</td>
<td>39.3</td>
<td>14</td>
<td>2.81</td>
<td>-648.495621346673</td>
<td>-0.260530</td>
<td>-0.064412</td>
</tr>
<tr>
<td>ORCA</td><td>3.0.1</td>
<td>33.7</td>
<td>13</td>
<td>2.59</td>
<td>-648.495620645754</td>
<td>-0.260533</td>
<td>-0.064445</td>
</tr>
<tr>
<td>Q-Chem</td><td>4.1.0.1</td>
<td>12.5</td>
<td>14</td>
<td>0.89</td>
<td>-648.495723730569</td>
<td>-0.260</td>
<td>-0.064</td>
</tr>
<tr>
<td>TURBOMOLE</td><td>6.5</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

**Machine:** Intel(R) Xeon E5-1620(R) @ 3.60 GHz running 64-bit Ubuntu 13.10

**Fancy compiler or maths libraries used when compiling:** Intel Parallel Studio XE 2013 SP1 (Compiler v14.0.1/MKL v11.1.1)

### HF
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th>
<th>Steps</th>
<th>per step</th>
<th>Total E</th>
<th>HOMO</th>
<th>LUMO</th>
</tr>
<tr>
<td>DALTON</td><td>2013.0</td>
<td>10.3</td>
<td>19</td>
<td>0.5</td>
<td>-644.675706212821</td>
<td>-0.35364477</td>
<td>0.07433447</td>
</tr>
<tr>
<td>MPQC</td><td>2.3.1, Ubuntu</td>
<td>28.3</td>
<td>28</td>
<td>1.0</td>
<td>-644.6757062224</td>
<td>-0.353644</td>
<td>0.074333</td>
</tr>
<tr>
<td>NWChem</td><td>6.3, Ubuntu</td>
<td>8.7</td>
<td>20</td>
<td>0.4</td>
<td>-644.675706609025</td>
<td>-0.3536110</td>
<td>0.07435021</td>
</tr>
<tr>
<td>ORCA</td><td>2.9.1</td>
<td>13</td>
<td>13</td>
<td>1.0</td>
<td>-644.675706036270</td>
<td>-0.353622</td>
<td>0.074344</td>
</tr>
<tr>
<td>ORCA</td><td>3.0.1</td>
<td>11</td>
<td>12</td>
<td>0.9</td>
<td>-644.675706036272</td>
<td>-0.353622</td>
<td>0.074344</td>
</tr>
<tr>
<td>Q-Chem</td><td>4.1.0.1, compiled</td>
<td>2.6</td>
<td>14</td>
<td>0.2</td>
<td>-644.675706161474</td>
<td>-0.354</td>
<td>0.074</td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th>
<th>Steps</th>
<th>per step</th>
<th>Total E</th>
<th>HOMO</th>
<th>LUMO</th>
</tr>
<tr>
<td>DALTON</td><td>2013.0</td>
<td>42.6</td>
<td>20</td>
<td>2.1</td>
<td>-648.4956905852</td>
<td>-0.26060842</td>
<td>-0.06441321</td>
</tr>
<tr>
<td>MPQC</td><td>2.3.1, Ubuntu</td>
<td>143.8</td>
<td>25</td>
<td>5.8</td>
<td>-648.4957002690</td>
<td>-0.260571</td>
<td>-0.064391</td>
</tr>
<tr>
<td>NWChem</td><td>6.3, Ubuntu</td>
<td>26</td>
<td>27</td>
<td>1.0</td>
<td>-648.495694167510</td>
<td>-0.2605703</td>
<td>-0.06439253</td>
</tr>
<tr>
<td>ORCA</td><td>2.9.1</td>
<td>18</td>
<td>14</td>
<td>1.3</td>
<td>-648.495621346649</td>
<td>-0.260530</td>
<td>-0.064412</td>
</tr>
<tr>
<td>ORCA</td><td>3.0.1</td>
<td>14.5</td>
<td>13</td>
<td>1.1</td>
<td>-648.495620645744</td>
<td>-0.260533</td>
<td>-0.064445</td>
</tr>
<tr>
<td>Q-Chem</td><td>4.1.0.1, compiled</td>
<td>4.8</td>
<td>14</td>
<td>0.3</td>
<td>-648.495723730572</td>
<td>-0.260</td>
<td>-0.064</td>
</tr>
</table>

Baoilleach's results
--------------------

**Machine:** Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz running 64-bit Centos 6.3

**Fancy compiler or maths libraries used when compiling:** None (system gcc, blas, lapack)

### HF
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale</td><td>r1013</td><td>810</td>
<td>90</td><td>9</td>
<td>-644.67570139</td>
<td>-0.353712</td>
<td>0.074269</td>
</tr>
<tr>
<td>NWChem</td><td>6.3</td><td>8.8</td>
<td>20</td><td>0.4</td>
<td>-644.67570661</td>
<td>-0.353611</td>
<td>0.074350</td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale</td><td>r1013</td><td>933</td>
<td>58</td><td>16.1</td>
<td>-648.49566820</td>
<td>-0.260899</td>
<td>-0.064457</td>
</tr>
<tr>
<td>NWChem</td><td>6.3</td><td>27.6</td>
<td>27</td><td>1.0</td>
<td>-648.495694167</td>
<td>-0.260570</td>
<td>-0.064393</td>
</tr>
</table>

Michael Banck's results
----------------------

**Machine:** Lenovo T400 (Intel(R) Core(TM)2 Duo CPU     P8400  @ 2.26GHz)

**Fancy compiler or maths libraries used when compiling:** Debian 7 packages

### HF
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale</td><td>r1013</td><td>3394</td>
<td>90</td><td>37.7</td>
<td>-644.67570139</td>
<td>-0.353712</td>
<td>0.074269</td>
</tr>
<tr>
<td>MPQC</td><td>2.3.1</td><td>64</td>
<td>28</td><td>2.3</td>
<td>-644.67570622</td>
<td>-0.353644</td>
<td>0.074333</td>
</tr>
<tr>
<td>PSI4</td><td>4.0beta5</td><td>115</td>
<td>16</td><td>7.2</td>
<td>-644.67570580</td>
<td>-0.353619</td>
<td>0.074353</td>
</tr>
<tr>
<td>NWChem</td><td>6.1</td><td>21</td>
<td>23</td><td>0.9</td>
<td>-644.67570680</td>
<td>-0.353608</td>
<td>0.074350</td>
</tr>
<tr>
<td>NWChem</td><td>6.3r2</td><td>19</td>
<td>20</td><td>1.0</td>
<td>-644.67570661</td>
<td>-0.353611</td>
<td>0.074350</td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale</td><td>r1013</td><td>9065</td>
<td>58</td><td>156.3</td>
<td>-648.495668200</td>
<td>-0.260899</td>
<td>-0.064457</td>
</tr>
<tr>
<td>MPQC</td><td>2.3.1</td><td>387</td>
<td>25</td><td>15.4</td>
<td>-648.495700269</td>
<td>-0.260571</td>
<td>-0.064391</td>
</tr>
<tr>
<td>PSI4</td><td>4.0beta5</td><td>190</td>
<td>16</td><td>11.9</td>
<td>-648.495697810</td>
<td>-0.260556</td>
<td>-0.064363</td>
</tr>
<tr>
<td>NWChem</td><td>6.1</td><td>56</td>
<td>27</td><td>2.1</td>
<td>-648.495694155</td>
<td>-0.260569</td>
<td>-0.064392</td>
</tr>
<tr>
<td>NWChem</td><td>6.3r2</td><td>55</td>
<td>27</td><td>2.0</td>
<td>-648.495694168</td>
<td>-0.260570</td>
<td>-0.064393</td>
</tr>
</table>

MY NAME HERE's results
----------------------

**Machine:** Description of one CPU and the OS

**Fancy compiler or maths libraries used when compiling:** Intel compiler? MKL?

### HF
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td></td><td></td>
<td></td><td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Version</th>
<th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td></td><td></td>
<td></td><td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>
