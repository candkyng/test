<h1>test-web-demo</h1>
<p>Create pytest framework with page object design pattern from scratch.</p>
<p>Invoke selenium automated test scenarios by Jenkins</p>

<h2>Run test</h2>
 <p>Ensure the following python packages are installed:</p>
 <ul>
 <li>selenium</li>
 <li>openpyxl</li>
 <li>pytest</li>
 </ul>
 <p>By default, chrome browser will be used. To run the test in Firefox or Edge, use  
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
 
 <h2>Integrate to Jenkins</h2>
 <p>Setup Jenkins using jenkins.war on windows platform:</p>
 <ol>
 <li>Get OpenJDK from <code>https://jdk.java.net</code>. 
 Click <a href="https://www.jenkins.io/doc/administration/requirements/java/">here</a> for Jenkins java requirement.
 <li>Get Jenkins Generic Java Package (jenkins.war) from <code>https://www.jenkins.io/download/</code></li>
 <li>In command prompt, run <code>java -jar jenkins.war -httpPort=9090</code></li>
 <li>Go to <code>http://localhost:9090</code> in web browser</li>
 <li>Enter initial admin password</li>
 <li>Click Install suggested plugins</li>
 <li>Create your own admin user or skip to use the default "admin" user and its initial admin password</li>
 </ol>
 <p>Configure job to run automated tests:</p>
 <ol>
 <li>Create a freestyle project</li>
 <li>Parameterize build with <i>Choice Parameter</i> called <i>browser</i></li>
 <li>Setup Source Code Management with github repository url</li>
 <li>Add <i>Execute Windows batch command</i> build step<br>
 <code>py.test --browser %browser% --html="report.html" --junitxml="result.xml"</code>
 </li>
 <li>Add <i>Publish JUnit test result report </i> (result.xml) Post-build Action. 
 Latest Test Result and Trend graph will be shown under project status every time after the project is built.</li>
 </ol>