$('#test').on('click', function (e) {
    alert('ok!');
});

$("#new_btn").on('click', function (e) {
    $('form.am-form-task')[0].reset();
    $('input.id').removeAttr('value');
    $('div.am-modal-task').modal();
    $('#my-alert').modal();
});


$.fn.datatableInit = function (columns, path, scrf, a,iDisplayLength) {
    var ocolumns = [];
    if (typeof(a) === 'undefined') {
        ocolumns.push(
            {
                "render": function (data, type, row) {
                    var html = "<div class=\"btn-group\">";
                    html += "<input type=\"checkbox\" name=\"cb\" value=\"" + row.id + "\">";
                    html += "</div>";
                    return html;
                }, "width": "5%"
            });
    }

    columns.forEach(function (val, index, arr) {
        ocolumns.push(
            {"mData": val}
        );
    });
    if (typeof(a) === 'undefined') {
        ocolumns.push(
            {
                "render": function (data, type, row) {
                    var id = '"' + row.id + '"';
                    var html = "<div class=\"am-btn-toolbar\">";
                    html += "<div class=\"am-btn-group am-btn-group-xs\">";
//                    html += "<button class=\"edit am-btn am-btn-default am-btn-xs am-text-secondary\"><span class=\"am-icon-pencil-square-o\"></span> 编辑</button>";
                    if (typeof(row.sync_flag) !== 'undefined') {
                        if (row.sync_flag !== 1) {
                            html += "<button class=\"edit am-btn am-btn-default am-btn-xs am-text-secondary\"><span class=\"am-icon-pencil-square-o\"></span> 编辑</button>";
                            html += "<button class=\"delete am-btn am-btn-default am-btn-xs am-text-danger am-hide-sm-only\"><span class=\"am-icon-trash-o\"></span> 删除</button>";
                        }
                    }
                    else {
                        html += "<button class=\"edit am-btn am-btn-default am-btn-xs am-text-secondary\"><span class=\"am-icon-pencil-square-o\"></span> 编辑</button>";
                        html += "<button class=\"delete am-btn am-btn-default am-btn-xs am-text-danger am-hide-sm-only\"><span class=\"am-icon-trash-o\"></span> 删除</button>";
                    }
                    html += "</div>";
                    html += "</div>";
                    return html;
                }, "width": "15%"
            }
        );
    }
    if (typeof(iDisplayLength) === 'undefined') {
        iDisplayLength = 100000
    }
    else {
        iDisplayLength = 20
    }
    var table = this.DataTable({
        "dom": '<"top"f >rt<"bottom"ilp><"clear"l>',//dom定位
        "processing": true,
        "serverSide": true,
        "bStateSave": true,
        "scrollY": "100%",
        "lengthChange": true,//是否允许用户自定义显示数量
        "bPaginate": true, //翻页功能
        "searching": false,//本地搜索
        "ordering": false, //排序功能
        "Info": false,//页脚信息
        "autoWidth": true,//自动宽度
        "bLengthChange": false,
        "iDisplayLength": iDisplayLength,
        "oLanguage": {//国际语言转化
            "sLengthMenu": "显示 _MENU_ 记录",
            "sZeroRecords": "对不起，查询不到任何相关数据",
            "sEmptyTable": "未有相关数据",
            "sLoadingRecords": "正在加载数据-请等待...",
            "sInfo": "当前显示 _START_ 到 _END_ 条，共 _TOTAL_ 条记录。",
            "sInfoEmpty": "当前显示0到0条，共0条记录",
            "sInfoFiltered": "（数据库中共为 _MAX_ 条记录）",
            "sProcessing": "正在加载数据...",
            "oPaginate": {
                "sFirst": "首页",
                "sPrevious": "<< ",
                "sNext": " >>",
                "sLast": " 尾页 "
            }
        },
        "sAjaxSource": "/" + path + "/source/",
        "fnServerData": function (sSource, aoData, fnCallback) {
            var keyword = $("input.keyword").val();
            if (keyword) {
                aoData.push({"name": "keyword", "value": keyword});
            }
            $.ajax({
                "contentType": "application/json; charset=utf-8",
                "url": sSource,
                "data": aoData,
                "success": fnCallback
            });
        },
        "aoColumns": ocolumns
    });
    table.on('click', 'button.edit', function (e) {
        e.preventDefault();
        var index = table.row($(this).parents('tr')).index();
        var data = table.data()[index];
        $('form.am-form-task').formEdit(data);
        $('div.am-modal-task').modal();
    });
    table.on('click', 'button.delete', function (e) {
        e.preventDefault();
        if (confirm("确定要删除该条记录？")) {
            var index = table.row($(this).parents('tr')).index();
            var data = table.data()[index];
            $.ajax({
                type: 'POST',
                url: '/' + path + '/delete/',
                data: {"csrfmiddlewaretoken": scrf, "id": data.id},
                success: function (data, status) {
                    if (!data.ret) {
                        alert('删除成功!');
                        table.row('.selected').remove().draw(false);
                    }
                    else {
                        alert(data.msg);
                    }
                },
                error: function (data) {
                    alert(data.status + ':' + data.statusText);
                }
            });
        }
    });
    $("button.search").bind('click', function () {
        table.ajax.reload();
    });

    $('form.am-form-task').submit(function (e) {
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '/' + path + '/save/',
            data: data,
            success: function (result, status) {
                if (!result.ret) {
                    table.draw(false);
                    $('div.am-modal-task').modal('close');
                }
                else {
                    alert(result.msg);
                }
            },
            error: function (result) {
                alert(result);
            }
        });
        return false;
    });


    $('form.am-form-upload').submit(function (e) {
        e.preventDefault();
        var data = $(this).serializeArray();
        var formData = new FormData();
        formData.append("file", document.getElementsByName("file")[0].files[0]);
        data.forEach(function (val, index, arr) {
            formData.append(val.name, val.value);
        });
        $.ajax({
            type: 'POST',
            url: '/' + path + '/upload/',
            data: formData,
            contentType: false,
            processData: false,
            success: function (result, status) {
                if (!result.ret) {
                    table.draw(false);
                    $('div.am-modal-upload').modal('close');
                }
                else {
                    alert(result.msg);
                }
            },
            error: function (result) {
                alert(result);
            }
        });
        return false;
    });

    $("button.batchdelete").bind('click', function () {
        if (confirm("确定要删除任务？")) {
            var ids = [];
            $("input[type='checkbox']").each(function () {
                if ($(this)[0]["checked"]) {
                    ids.push($(this)[0]["value"])
                }
            });
            $.ajax({
                type: 'POST',
                url: "/" + path + "/batchdelete/",
                data: 'ids=' + ids,
                success: function (data, status) {
                    if (!data.ret) {
                        alert('删除任务成功!');
                        table.row('.selected').remove().draw(false);
                    }
                    else {
                        alert("删除任务失败!失败原因:" + data.msg);
                    }
                },
                error: function (data) {
                    alert("删除任务错误!错误信息:" + data.status + ':' + data.statusText);
                }
            });
        }
    });
    $("button.download").bind('click', function () {
        window.open("http://52.80.104.236:8082/static/assets/template.csv");
    });
    $("button.download_register").bind('click', function () {
        window.open("http://52.80.104.236:8082/static/assets/register.csv");
    });
};