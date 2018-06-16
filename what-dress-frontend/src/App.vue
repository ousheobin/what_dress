<template>
  <div id="app">
    <el-container>
      <el-header
        height="60px"
        :style="{ 'background-color': '#6ecfd3' ,'width':'100%' }"
        class="header"
        >
        <p class="header-title">Tentcoo Dress AI</p>
      </el-header>
      <el-main style="margin:0px; padding:0px">
        <router-view style="min-height:100px;"/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Api from '@/api/Api';
export default {
  name: 'App',
  mounted: function(){
    
  },
  data () {
    return {
      
    }
  },
  methods:{

  }
}
</script>
