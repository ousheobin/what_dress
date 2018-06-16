<template>
  <div style="text-align:center;">
    <h1>识别的图片</h1>
    <img :src="fileUrl" style="max-height:300px; width:auto; margin:10px auto;">
    <div>
        <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
            prop="type"
            header-align="center"
            label="识别项目">
            </el-table-column>
            <el-table-column
            prop="label"
            header-align="center"
            label="识别结果">
            </el-table-column>
            <el-table-column
            prop="score"
            header-align="center"
            label="置信度">
            </el-table-column>
        </el-table>
    </div>
    <div style="margin:20px;">
        <el-button type="primary" style="width:100px;" @click="onBackBtnClick">返回</el-button>  
    </div>
    
  </div>
</template>
<script>
export default {
    mounted(){
        var skirtAndPantIndex = 0
        if(this.$route.params.result.skirtAndPantLegnth[0].label == '判断不出来'){
            if(parseFloat(this.$route.params.result.skirtAndPantLegnth[1].score) > 0.45){
                skirtAndPantIndex ++;
            }
        }
        this.$data.tableData.push({
            'type':'裙装/裤装',
            'label': this.$route.params.result.skirtAndPantLegnth[skirtAndPantIndex].label,
            'score': this.$route.params.result.skirtAndPantLegnth[skirtAndPantIndex].score,
        })
        var sleeveLengthIndex = 0
        if(this.$route.params.result.sleeveLength[0].label == '判断不出来'){
            if(parseFloat(this.$route.params.result.sleeveLength[1].score) > 0.45){
                sleeveLengthIndex ++;
            }
        }
        this.$data.tableData.push({
            'type':'衣服袖子',
            'label': this.$route.params.result.sleeveLength[sleeveLengthIndex].label,
            'score': this.$route.params.result.sleeveLength[sleeveLengthIndex].score,
        })
        this.$data.fileUrl = this.$route.params.file.url
    },
    data(){
        return{
            tableData: [],
            fileUrl: ''
        }
    },
    methods: {
        onBackBtnClick(){
            this.$router.push({
                path:"/",
            });
        }
    }
}
</script>
