Quantum Chemistry Speed Test
============================

**The rules**: Calculations must only use a single CPU. The B3LYP used should be that used by default by Gaussian and NWChem (namely the VWN3 not VWN5). And please, no Gaussian input files or results.

Various people have submitted results:
- [Eric Berquist](http://github.com/berky/qmspeedtest)
- [Michael Banck](http://github.com/mbanck/qmspeedtest)
- [Noel O'Boyle](http://github.com/baoilleach/qmspeedtest)
- [Pedro Silva](http://github.com/PedroJSilva/qmspeedtest)

Please fork the [original repo](http://github.com/baoilleach/qmspeedtest) and submit your own!

Baoilleach's results
--------------------

**Machine:** Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz running 64-bit Centos 6.3

**Fancy compiler or maths libraries used when compiling:** None (system gcc, blas, lapack)

### HF
<table>
<tr>
<th>QM Package</th><th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale r1013</td><td>810</td>
<td>90</td><td>9</td>
<td>-644.67570139</td>
<td>-0.353712</td>
<td>0.074269</td>
</tr>
<tr>
<td>NWChem 6.3</td><td>8.5</td>
<td>19</td><td>0.4</td>
<td>-644.67570661</td>
<td>-0.3536105</td>
<td>0.07435040</td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale r1013</td><td>933</td>
<td>58</td><td>16.1</td>
<td>-648.49566820</td>
<td>-0.260899</td>
<td>-0.064457</td>
</tr>
<tr>
<td>NWChem 6.3</td><td>17.0</td>
<td>19</td><td>0.9</td>
<td>-648.49569450</td>
<td>-0.2605941</td>
<td>-0.06439398</td>
</tr>
</table>

Michael Banck's results
----------------------

**Machine:** Lenovo T400 (Intel(R) Core(TM)2 Duo CPU     P8400  @ 2.26GHz)

**Fancy compiler or maths libraries used when compiling:** Debian 7 packages

### HF
<table>
<tr>
<th>QM Package</th><th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale r1013</td><td>3394</td>
<td>90</td><td>37.7</td>
<td>-644.67570139</td>
<td>-0.353712</td>
<td>0.074269</td>
</tr>
<tr>
<td>MPQC 2.3.1</td><td>64</td>
<td>28</td><td>2.3</td>
<td>-644.67570622</td>
<td>-0.353644</td>
<td>0.074333</td>
</tr>
<tr>
<td>PSI4 4.0beta5</td><td>115</td>
<td>16</td><td>7.2</td>
<td>-644.67570580</td>
<td>-0.353619</td>
<td>0.074353</td>
</tr>
<tr>
<td>NWChem 6.1</td><td>21</td>
<td>23</td><td>0.9</td>
<td>-644.67570680</td>
<td>-0.353608</td>
<td>0.074350</td>
</tr>
<tr>
<td>NWChem 6.3r2</td><td>19</td>
<td>20</td><td>1.0</td>
<td>-644.67570661</td>
<td>-0.353611</td>
<td>0.074350</td>
</tr>
</table>

### B3LYP
<table>
<tr>
<th>QM Package</th><th>Time (min)</th><th>Steps</th><th>per step</th>
<th>Total E</th><th>HOMO</th><th>LUMO</th>
</tr>
<tr>
<td>erkale r1013</td><td>9065</td>
<td>58</td><td>156.3</td>
<td>-648.495668200</td>
<td>-0.260899</td>
<td>-0.064457</td>
</tr>
<tr>
<td>MPQC 2.3.1</td><td>387</td>
<td>25</td><td>15.4</td>
<td>-648.495700269</td>
<td>-0.260571</td>
<td>-0.064391</td>
</tr>
<tr>
<td>PSI4 4.0beta5</td><td>190</td>
<td>16</td><td>11.9</td>
<td>-648.495697810</td>
<td>-0.260556</td>
<td>-0.064363</td>
</tr>
<tr>
<td>NWChem 6.1</td><td>56</td>
<td>27</td><td>2.1</td>
<td>-648.495694155</td>
<td>-0.260569</td>
<td>-0.064392</td>
</tr>
<tr>
<td>NWChem 6.3r2</td><td>55</td>
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
<th>QM Package</th><th>Time (min)</th><th>Steps</th><th>per step</th>
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
<th>QM Package</th><th>Time (min)</th><th>Steps</th><th>per step</th>
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
