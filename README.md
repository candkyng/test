<h1>test-web-demo</h1>
<p>Create pytest framework with page object design pattern and demo selenium automated test scenarios</p>


 
 <h2>Run test</h2>
 <p> </p>
 <p>By default, chrome browser will be used. To run in Firefox or Edge, use  
 <code>--browser</code> option:  
 
 <code>py.test --browser edge</code><br><br>
 <code>py.text --browser firefox</code>
 </p>
  <p>Note for Edge: Please update the Edge WebDriver name to be MicrosoftWebDriver.exe so that 
  the default execution path can be used when creating a new instance of Edge driver.
 </p>
 
 <p>To override test url, use <code>--url</code> option</p>
 <code>py.test --url <i>url</i></code>
 
 <h2>Create test report</h2>
 <p>To generate test report, install pytest-html package: 
 <code>pip install pytest-html</code></p>
 <p>Run tests with <code>--html</code> option <br><br>
 <code>py.test --html="report.html"</code> <br><br>
 Test report <b>report.html</b> will be generated under the current directory.
 </p>