修改获取考试安排的方式，首先 get 请求调用http://zhjw.qfnu.edu.cn/jsxsd/xsks/xsksap_query，解析html，找到现在的默认学期，该学期就是默认学期就是目标学期
下面是示例 html

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
  <head id="headerid1">
    <base target="_self" />
    <title>我的考试 - 考试安排查询</title>
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="keywords" content="湖南强智科技教务系统" />
    <meta http-equiv="description" content="湖南强智科技教务系统" />
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8" />
    <script
      type="text/javascript"
      src="/jsxsd/js/jquery-1.8.0.min.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/jquery-min.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/common.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/iepngfix_tilebg.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/easyui/jquery.easyui.min.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/jquery.autocomplete.min.js"
      language="javascript"></script>
    <link
      href="/jsxsd/framework/images/common.css"
      rel="stylesheet"
      type="text/css" />
    <link
      href="/jsxsd/framework/images/blue.css"
      rel="stylesheet"
      type="text/css"
      id="link_theme" />
    <link
      href="/jsxsd/framework/images/workstation.css"
      rel="stylesheet"
      type="text/css" />
    <link href="/jsxsd/css/easyui.css" rel="stylesheet" type="text/css" />
    <link
      href="/jsxsd/css/jquery.autocomplete.css"
      rel="stylesheet"
      type="text/css" />
  </head>
  <iframe
    id="notSession"
    name="notSession"
    style="display: none;"
    src=""></iframe>
  <script type="text/javascript">
    jQuery(document).ready(function () {
      window.setInterval(function () {
        document.getElementById("notSession").src =
          "/jsxsd/framework/blankPage.jsp";
      }, 1000 * 60 * 10);
    });
  </script>
  <body style="height: 750px;">
    <div class="Nsb_pw">
      <div class="Nsb_layout_r">
        <div class="Nsb_layout_r title">考试安排查询</div>
        <form
          action=""
          name="ksapQueryForm"
          id="ksapQueryForm"
          method="post"
          target="fcenter">
          <input type="hidden" id="xqlbmc" name="xqlbmc" value="" />
          <input type="hidden" id="sxxnxq" name="sxxnxq" value="" />
          <input type="hidden" id="dqxnxq" name="dqxnxq" value="" />
          <input type="hidden" id="ckbz" name="ckbz" value="" />
          <table
            width="100%"
            border="0"
            cellspacing="0"
            cellpadding="0"
            class="no_border_table">
            <tr>
              <th width="80px" align="right">学年学期：</th>

              <td width="160px">
                <select id="xnxqid" name="xnxqid" style="width: 150px;">
                  <option value="2025-2026-2">2025-2026-2</option>

                  <option selected value="2025-2026-1">2025-2026-1</option>

                  <option value="2024-2025-3">2024-2025-3</option>

                  <option value="2024-2025-2">2024-2025-2</option>

                  <option value="2024-2025-1">2024-2025-1</option>

                  <option value="2023-2024-3">2023-2024-3</option>

                  <option value="2023-2024-2">2023-2024-2</option>

                  <option value="2023-2024-1">2023-2024-1</option>

                  <option value="2022-2023-3">2022-2023-3</option>

                  <option value="2022-2023-2">2022-2023-2</option>

                  <option value="2022-2023-1">2022-2023-1</option>

                  <option value="2021-2022-3">2021-2022-3</option>

                  <option value="2021-2022-2">2021-2022-2</option>

                  <option value="2021-2022-1">2021-2022-1</option>

                  <option value="2020-2021-2">2020-2021-2</option>

                  <option value="2020-2021-1">2020-2021-1</option>

                  <option value="2019-2020-3">2019-2020-3</option>

                  <option value="2019-2020-2">2019-2020-2</option>

                  <option value="2019-2020-1">2019-2020-1</option>

                  <option value="2018-2019-2">2018-2019-2</option>

                  <option value="2018-2019-1">2018-2019-1</option>

                  <option value="2017-2018-2">2017-2018-2</option>

                  <option value="2017-2018-1">2017-2018-1</option>

                  <option value="2016-2017-2">2016-2017-2</option>

                  <option value="2016-2017-1">2016-2017-1</option>

                  <option value="2015-2016-2">2015-2016-2</option>

                  <option value="2015-2016-1">2015-2016-1</option>

                  <option value="2014-2015-2">2014-2015-2</option>

                  <option value="2014-2015-1">2014-2015-1</option>

                  <option value="2013-2014-2">2013-2014-2</option>

                  <option value="2013-2014-1">2013-2014-1</option>

                  <option value="2012-2013-2">2012-2013-2</option>

                  <option value="2012-2013-1">2012-2013-1</option>

                  <option value="2011-2012-2">2011-2012-2</option>

                  <option value="2011-2012-1">2011-2012-1</option>

                  <option value="2010-2011-2">2010-2011-2</option>

                  <option value="2010-2011-1">2010-2011-1</option>

                  <option value="2009-2010-2">2009-2010-2</option>

                  <option value="2009-2010-1">2009-2010-1</option>

                  <option value="2008-2009-2">2008-2009-2</option>

                  <option value="2008-2009-1">2008-2009-1</option>

                  <option value="2007-2008-2">2007-2008-2</option>

                  <option value="2007-2008-1">2007-2008-1</option>
                </select>
              </td>

              <th width="70px" align="right">学期类别：</th>
              <td width="160px">
                <select id="xqlb" name="xqlb" style="width: 150px;">
                  <option value="">---请选择---</option>

                  <option value="1">期初</option>

                  <option value="2">期中</option>

                  <option value="3">期末</option>
                </select>
              </td>

              <td>
                <input
                  type="button"
                  id="btn_query"
                  value="查 询"
                  onclick="queryKsap()"
                  class="button el-button" />
              </td>
            </tr>
          </table>
        </form>
      </div>
    </div>
    <div id="frameView" style="width:100%;HEIGHT:100%">
      <iframe
        frameborder="0"
        id="fcenter"
        name="fcenter"
        style="HEIGHT:100%;width:100%;"
        scrolling="auto"></iframe>
    </div>
    <form action="" name="Formfr" id="FormFr">
      <input type="hidden" name="key" id="key" />
    </form>

    <input id="PageContext" type="hidden" value="/jsxsd" />
    <script
      type="text/javascript"
      src="/jsxsd/js/validate.js"
      language="javascript"></script>
    <script language="javascript">
      function queryKsap() {
        if (jQuery("#xqlb").val() != "") {
          jQuery("#xqlbmc").val(jQuery("#xqlb option:selected").text());
        }
        document.forms["ksapQueryForm"].action = "/jsxsd/xsks/xsksap_list";
        document.forms["ksapQueryForm"].submit();
      }
      loadjs();
      function loadjs() {
        if ("" != "") {
          alert("");
        }
      }

      function viewKsxz() {
        //NEW_XSD_KSBM_WDKS_KSAPCX_KSXZCK
        var sxxnxq = $("#sxxnxq").val(); //生效学年学期
        var xzxnxq = $("#xnxqid_0").val(); //选择学年学期
        if (sxxnxq != xzxnxq) {
          alert("当前学年学期未启用考试须知查看！");
        } else {
          var url = "/jsxsd/xsks/ksxzView";
          window.open(
            url,
            "newwindow",
            "height=600,width=794,top=50,left=200,toolbar=no,menubar=no,location=no, status=no"
          );
        }
      }

      function gradeChange() {
        var xzxnxq = $("select  option:selected").val(); //选择学年学期
        var sxxnxq = $("#sxxnxq").val(); //生效学年学期
        var dqxnxq = $("#dqxnxq").val(); //当前学年学期
        var ckbz = $("#ckbz").val(); //查看状态
        console.log("选择学年学期", xzxnxq);
        console.log("生效学年学期", sxxnxq);
        console.log("当前学年学期", dqxnxq);
        console.log("查看状态", ckbz);
        if (dqxnxq != sxxnxq) {
          if (sxxnxq != xzxnxq) {
            document.getElementById("btn_query_2").disabled = false;
          } else {
            if (ckbz == "1") {
              document.getElementById("btn_query_2").disabled = true;
            } else {
              document.getElementById("btn_query_2").disabled = false;
            }
          }
        } else {
          if (sxxnxq != xzxnxq) {
            if (ckbz == "1") {
              document.getElementById("btn_query_0").disabled = false;
            } else {
              document.getElementById("btn_query_1").disabled = false;
            }
          } else {
            if (ckbz == "1") {
              document.getElementById("btn_query_0").disabled = true;
            } else {
              document.getElementById("btn_query_1").disabled = true;
            }
          }
        }
      }

      function kzbb() {
        var xnxqid = $("#xnxqid").val();
        var xqlb = $("#xqlb").val();
        if (xnxqid == null || xnxqid == undefined || xnxqid == "") {
          alert("请选择学年学期！");
          return false;
        }
        if (xqlb == null || xqlb == undefined || xqlb == "") {
          alert("请选择学期类别！");
          return false;
        }
        var cs = xnxqid + "," + xqlb + "," + "2022416246";
        rqdy_laosha(
          cs,
          "辽宁警察学院_学生端准考证打印",
          "null",
          "alert('无对应润乾模板配置')"
        );
      }
    </script>
  </body>
</html>
```

解析方式：找到 select 标签，获取被选中的 option 的 value 值，就是目标学期

然后 post 请求调用 http://zhjw.qfnu.edu.cn/jsxsd/xsks/xsksap_list ，解析考试安排，下面是示例 html

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head id="headerid1">
    <base target="_self" />
    <title>我的考试 - 考试安排查询</title>
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="keywords" content="湖南强智科技教务系统" />
    <meta http-equiv="description" content="湖南强智科技教务系统" />
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8" />
    <script
      type="text/javascript"
      src="/jsxsd/js/jquery-1.8.0.min.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/jquery-min.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/common.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/iepngfix_tilebg.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/easyui/jquery.easyui.min.js"
      language="javascript"></script>
    <script
      type="text/javascript"
      src="/jsxsd/js/jquery.autocomplete.min.js"
      language="javascript"></script>
    <link
      href="/jsxsd/framework/images/common.css"
      rel="stylesheet"
      type="text/css" />
    <link
      href="/jsxsd/framework/images/blue.css"
      rel="stylesheet"
      type="text/css"
      id="link_theme" />
    <link
      href="/jsxsd/framework/images/workstation.css"
      rel="stylesheet"
      type="text/css" />
    <link href="/jsxsd/css/easyui.css" rel="stylesheet" type="text/css" />
    <link
      href="/jsxsd/css/jquery.autocomplete.css"
      rel="stylesheet"
      type="text/css" />
  </head>
  <iframe
    id="notSession"
    name="notSession"
    style="display: none;"
    src=""></iframe>
  <script type="text/javascript">
    jQuery(document).ready(function () {
      window.setInterval(function () {
        document.getElementById("notSession").src =
          "/jsxsd/framework/blankPage.jsp";
      }, 1000 * 60 * 10);
    });
  </script>
  <body>
    <script>
      .MHover{
          border:1px solid #ccc;
          white-space:nowrap;
          text-overflow:ellipsis;
          overflow:hidden;
      }
    </script>

    <div class="Nsb_pw">
      <br />

      <table
        id="dataList"
        width="100%"
        border="0"
        cellspacing="0"
        cellpadding="0"
        class="Nsb_r_list Nsb_table">
        <tr>
          <th class="Nsb_r_list_thb" style="width: 35px;">序号</th>
          <th class="Nsb_r_list_thb" style="width: 80px;">校区</th>
          <th class="Nsb_r_list_thb" style="width: 120px;">考试场次</th>
          <th class="Nsb_r_list_thb" style="width: 120px;">课程编号</th>
          <th class="Nsb_r_list_thb" style="width: 160px;">课程名称</th>
          <th class="Nsb_r_list_thb" style="width: 110px;">授课教师</th>
          <th class="Nsb_r_list_thb">考试时间</th>
          <th class="Nsb_r_list_thb" style="width: 140px;">考场</th>
          <th class="Nsb_r_list_thb" style="width: 60px;">座位号</th>
          <th class="Nsb_r_list_thb" style="width: 120px;">准考证号</th>
          <th class="Nsb_r_list_thb" style="width: 120px;">备注</th>
          <th class="Nsb_r_list_thb" style="width: 50px;">操作</th>
        </tr>

        <tr>
          <td colspan="10">未查询到数据</td>
        </tr>
      </table>
    </div>
    <br />

    <script language="javascript">
      function fuc(obj) {
        JsMod("/jsxsd/xsks/xsksap_bz.do?kw0410id=" + obj);
      }

      $(document).ready(function () {
        $(".MALL").hide();
        $(".MHover").mouseover(function (e) {
          $(this)
            .next(".MALL")
            .css({ position: "absolute", top: e.pageY + 5, left: e.pageX + 5 })
            .show();
        });
        $(".MHover").mousemove(function (e) {
          $(this)
            .next(".MALL")
            .css({
              color: "fff",
              position: "absolute",
              opacity: "1.0",
              "background-color": "#F0FFFF",
              top: e.pageY + 5,
              left: e.pageX + 5,
            });
        });
        $(".MHover").mouseout(function () {
          $(this).next(".MALL").hide();
        });
      });
    </script>
  </body>
</html>
```

解析方式：找到 table 标签，遍历 tr 标签，跳过第一个表头行，解析后续行的各个 td 标签，分别对应考试安排的信息字段