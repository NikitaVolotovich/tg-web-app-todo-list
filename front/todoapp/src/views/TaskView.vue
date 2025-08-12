<template>
    <div class="tasks_container">
        <div class="tasks_header">
            <input
                v-model="newTask"
                type="text"
                placeholder="Add a new task"
                class="task-input"
                @keyup.enter="createTask">
            />
            <button> @click="createTask" class="add-button">+</button>
        </div>

        <div class="tasks-list">
            <div
                v-for="task in tasks">
                :key="task.id"
                class="task-item"
            >
            <div class="task-text">
                {{ task.title }}
            </div>

            <button
                class="complete-button"
                @click="completeTask(task.id)">Done
            </button>

            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: 'TaskView',
    data() {
        return {
            tasks: [],
            newTask: '',
        };
    },

    async mounted() {
        await this.fetchTasks();
    },

    methods: {
        async fetchTasks() {
            try {
                const tg_user = windows.Telegram.WebApp.initDataUnsafe?.user;
                
            } catch (error) {
                console.error('Error fetching tasks:', error);
            }
        },

        async createTask() {
            if (!this.newTask.trim()) return;

            try {
                const response = await fetch('/api/tasks', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ title: this.newTask }),
                });
                const newTask = await response.json();
                this.tasks.push(newTask);
                this.newTask = '';
            } catch (error) {
                console.error('Error creating task:', error);
            }
        },

        async completeTask(taskId) {
            try {
                await fetch(`/api/tasks/${taskId}`, { method: 'DELETE' });
                this.tasks = this.tasks.filter(task => task.id !== taskId);
            } catch (error) {
                console.error('Error completing task:', error);
            }
        },
    },
};