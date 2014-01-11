qmspeedtest
===========

Quantum Chemistry speed test. Note that it must only use a single CPU. And please, no Gaussian results.

Eric Berquist's results
----------------------

**Machine:** Intel(R) Xeon E5-1620(R) @ 3.60 GHz running 64-bit Ubuntu 13.10

**Fancy compiler or maths libraries used when compiling:** Intel Parallel Studio XE 2013 SP1 (Compiler v14.0.1/MKL v11.1.1)

### HF
<table>
<tr>
<th>QM Package</th>
<th>Time (min)</th>
<th>Steps</th>
<th>per step</th>
<th>Total E</th>
<th>HOMO</th>
<th>LUMO</th>
</tr>
<tr>
<td>DALTON (2013.0)</td>
<td>10.3</td>
<td>19</td>
<td>0.5</td>
<td>-644.675706212821</td>
<td>-0.35364477</td>
<td>0.07433447</td>
</tr>
<tr>
<td>MPQC (2.3.1, Ubuntu)</td>
<td>28.3</td>
<td>28</td>
<td>1.0</td>
<td>-644.6757062224</td>
<td>-0.353644</td>
<td>0.074333</td>
</tr>
<tr>
<td>NWChem (6.3, Ubuntu)</td>
<td>8.7</td>
<td>20</td>
<td>0.4</td>
<td>-644.675706609025</td>
<td>-0.3536110</td>
<td>0.07435021</td>
</tr>
<tr>
<td>ORCA (2.9.1)</td>
<td>13</td>
<td>13</td>
<td>1.0</td>
<td>-644.675706036270</td>
<td>-0.353622</td>
<td>0.074344</td>
</tr>
<tr>
<td>ORCA (3.0.1)</td>
<td>11</td>
<td>12</td>
<td>0.9</td>
<td>-644.675706036272</td>
<td>-0.353622</td>
<td>0.074344</td>
</tr>
<tr>
<td>Q-Chem (4.1.0.1, compiled)</td>
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
<th>QM Package</th>
<th>Time (min)</th>
<th>Steps</th>
<th>per step</th>
<th>Total E</th>
<th>HOMO</th>
<th>LUMO</th>
</tr>
<tr>
<td>DALTON (2013.0)</td>
<td>42.2</td>
<td>20</td>
<td>2.1</td>
<td>-648.146520813871</td>
<td>-0.25714248</td>
<td>-0.06101431</td>
</tr>
<tr>
<td>MPQC (2.3.1, Ubuntu)</td>
<td>143.8</td>
<td>25</td>
<td>5.8</td>
<td>-648.4957002690</td>
<td>-0.260571</td>
<td>-0.064391</td>
</tr>
<tr>
<td>NWChem (6.3, Ubuntu)</td>
<td>26</td>
<td>27</td>
<td>1.0</td>
<td>-648.495694167510</td>
<td>-0.2605703</td>
<td>-0.06439253</td>
</tr>
<tr>
<td>ORCA (2.9.1)</td>
<td>18</td>
<td>14</td>
<td>1.3</td>
<td>-648.495621346649</td>
<td>-0.260530</td>
<td>-0.064412</td>
</tr>
<tr>
<td>ORCA (3.0.1)</td>
<td>14.5</td>
<td>13</td>
<td>1.1</td>
<td>-648.495620645744</td>
<td>-0.260533</td>
<td>-0.064445</td>
</tr>
<tr>
<td>Q-Chem (4.1.0.1, compiled)</td>
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
